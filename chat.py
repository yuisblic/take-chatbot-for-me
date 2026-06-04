import streamlit as st
from dotenv import load_dotenv
from llm import get_ai_response

st.set_page_config(page_title="(take)API 검색기", page_icon="🤖")

st.title("🤖 API 검색기")
st.caption("API에 관련된 모든 것을 답해드립니다.")

load_dotenv()

# session state
if "message_list" not in st.session_state:
    st.session_state.message_list = []

# 히스토리 출력
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 질문 입력
if user_question := st.chat_input("API 관련 질문을 입력하세요"):

    # user 출력
    st.chat_message("user").markdown(user_question)
    st.session_state.message_list.append(
        {"role": "user", "content": user_question}
    )

    with st.spinner("답변 생성 중..."):
        ai_response = get_ai_response(user_question)

        # 🔥 assistant 출력 (핵심)
        with st.chat_message("assistant"):
            st.markdown(ai_response)

        # 히스토리 저장
        st.session_state.message_list.append(
            {"role": "assistant", "content": ai_response}
        )