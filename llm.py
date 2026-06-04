from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, FewShotChatMessagePromptTemplate
import os
from langchain_upstage import ChatUpstage
from langchain_upstage import UpstageEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from config import answer_examples

store = {}

# Session History 관리 함수
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


def get_retriever():
    embeddings = UpstageEmbeddings(model="solar-embedding-1-large")
    index_name = 'take-guide-index'
    database = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)
    retriever = database.as_retriever()

    return retriever


def get_history_retriever():
    llm = get_llm()
    retriever = get_retriever()

    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as is."
    )

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )  

    return history_aware_retriever


def get_llm():
    llm = ChatUpstage()
    return llm


def get_rag_chain():
    
    llm = get_llm()

    # Few shot 작업
    example_prompt = ChatPromptTemplate.from_messages(
        [
            ("human", "{input}"),
            ("ai", "{answer}"),
        ]
    )
    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=answer_examples
    )

    # 채팅 히스토리 작업
    system_prompt = ("""
        당신은 UXBooster API 문서 전문가입니다.

        규칙:
        1. 반드시 제공된 Context 문서만 사용하세요.
        2. 문서에 없는 내용은 추측하지 마세요.
        3. 관련 API가 없다면 "관련 API를 찾을 수 없습니다."라고 답변하세요.
        4. API 이름을 먼저 제시하세요.
        5. API 설명을 제공하세요.
        6. Parameter 정보를 표로 정리하세요.
        7. Return 정보를 표로 정리하세요.
        8. 예제가 있으면 함께 제공하세요.

        {context}
        """
        )
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            few_shot_prompt,
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    history_aware_retriever = get_history_retriever()
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    ).pick('answer')

    return conversational_rag_chain


def get_ai_response(user_message : str) -> str:
    
    rag_chain = get_rag_chain()

    response = rag_chain.stream(
        {"input": user_message},
        config={"configurable": {"session_id": "abc123"}},
        )

    return response