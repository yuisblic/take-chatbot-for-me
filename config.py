answer_examples = [
    {
        "input": "dataset을 list 형태로 조회하는 API가 있나요?",
        "answer": """
        API명: getObjectList

        DataSet을 List<T> 객체로 변환하여 조회하는 API입니다.

        Nexacro에서 전달된 DataSet을 List<T> 형태로 반환합니다.

        | Parameter Type | Parameter | Param설명 | Return Type |
        | --- | --- | --- | --- |
        | String | datasetId | DataSet ID | List<T> |

        ### Example

        ```java
        List<BoardInfo> boardList =
            takeDataRequest.getObjectList(
                "dsBoard",
                BoardInfo.class
            );"""
    },
    {
        "input": "dataset을 객체 형태로 가져오는 API가 있나요?",
        "answer": """
        API명: getObject

        DataSet의 단일 데이터를 객체(Object) 형태로 조회하는 API입니다.

        Nexacro에서 전달된 DataSet을 지정한 객체 타입으로 반환합니다.

        | Parameter Type | Parameter | Param설명    | Return Type |
        | -------------- | --------- | ---------- | ----------- |
        | String         | datasetId | DataSet ID | T           |

        ### Example

        ```java
        BoardInfo boardInfo =
            takeDataRequest.getObject(
                "dsBoard",
                BoardInfo.class
            );

        """
    },
    {
        "input": "파라미터 값을 조회하는 API가 있나요?",
        "answer": """
        API명: getParameter

        Nexacro에서 전달한 Parameter 값을 조회하는 API입니다.

        지정한 Parameter의 값을 반환합니다.

        | Parameter Type | Parameter     | Param설명      | Return Type |
        | -------------- | ------------- | ------------ | ----------- |
        | String         | parameterName | Parameter 이름 | String      |

        ### Example
        
        ```java
        String userId =
            takeDataRequest.getParameter(
                "userId"
            );
        """
    },
]