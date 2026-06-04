**UXBooster 주요 API 설명**

Version Release 1.6

**목 차**

[1\. Take Java API 6](#_Toc166161512)

[1.1 TakeDataRequest.java 6](#_Toc166161513)

[1.1.1 getParamMap 6](#_Toc166161514)

[1.1.2 getMapList 6](#_Toc166161515)

[1.1.3 getOriginalMapList 7](#_Toc166161516)

[1.1.4 getDataSet 7](#_Toc166161517)

[1.1.5 getDataSetList 8](#_Toc166161518)

[1.1.6 getDataSets 8](#_Toc166161519)

[1.1.7 getObjectList 9](#_Toc166161520)

[1.1.8 getPrimitiveList 9](#_Toc166161521)

[1.1.9 getString 9](#_Toc166161522)

[1.2 TakeDataResponse.java 10](#_Toc166161523)

[1.2.1 addDataSet 10](#_Toc166161524)

[1.2.2 addParam 10](#_Toc166161525)

[1.2.3 addParam 11](#_Toc166161526)

[1.2.4 addPagingDataSet 11](#_Toc166161527)

[1.2.5 success 12](#_Toc166161528)

[1.2.6 error 12](#_Toc166161529)

[1.2.7 error 12](#_Toc166161530)

[1.2.8 write 13](#_Toc166161531)

[1.2.9 write 13](#_Toc166161532)

[2\. Take JS Function 구성 14](#_Toc166161533)

[2.1 ComponentList 14](#_Toc166161534)

[2.2 isQuickView 14](#_Toc166161535)

[2.3 ObjectPath 14](#_Toc166161536)

[2.4 isNull 15](#_Toc166161537)

[2.5 isFunction 15](#_Toc166161538)

[2.6 getTodayTime 15](#_Toc166161539)

[2.7 ObjectType 16](#_Toc166161540)

[2.8 CompTypeName 16](#_Toc166161541)

[2.9 CompType 16](#_Toc166161542)

[2.10 setComma 17](#_Toc166161543)

[2.11 getByteLength 17](#_Toc166161544)

[2.12 isEmail 17](#_Toc166161545)

[2.13 isDate 18](#_Toc166161546)

[2.14 isFromTo 18](#_Toc166161547)

[2.15 replaceFormat 18](#_Toc166161548)

[2.16 decode 19](#_Toc166161549)

[2.17 getUniqueId 19](#_Toc166161550)

[2.18 getSequenceId 19](#_Toc166161551)

[2.19 ArrayPluck 20](#_Toc166161552)

[2.20 getTextlimitTo 20](#_Toc166161553)

[2.21 getFunctionName 21](#_Toc166161554)

[2.22 debug 21](#_Toc166161555)

[2.23 error 21](#_Toc166161556)

[2.24 trace 22](#_Toc166161557)

[2.25 alert 22](#_Toc166161558)

[2.26 confirm 23](#_Toc166161559)

[2.27 setLocalData 23](#_Toc166161560)

[2.28 getLoc](#_Toc166161561)[alData 23](#_Toc166161561)

[2.29 getBindColName 24](#_Toc166161562)

[2.30 formOnLoad 24](#_Toc166161563)

[2.31 formRole 24](#_Toc166161564)

[2.32 svcFindReplace 25](#_Toc166161565)

[2.33 transaction 25](#_Toc166161566)

[2.34 tranCallBack 25](#_Toc166161567)

[2.35 tranSelect 26](#_Toc166161568)

[2.36 tranCode 26](#_Toc166161569)

[2.37 openPopup 27](#_Toc166161570)

[2.38 dataSelPopUp 27](#_Toc166161571)

[2.39 nvl 28](#_Toc166161572)

[2.40 isNumber 28](#_Toc166161573)

[2.41 getUser 29](#_Toc166161574)

[2.42 isStudio 29](#_Toc166161575)

[2.43 getOwnerForm 29](#_Toc166161576)

[2.44 getActiveForm 29](#_Toc166161577)

[2.45 getParentForm 30](#_Toc166161578)

[2.46 getConvertDate 30](#_Toc166161579)

[2.47 getDateWeek 30](#_Toc166161580)

[2.48 getDateTerm 31](#_Toc166161581)

[2.49 isLeapYear 31](#_Toc166161582)

[2.50 getDaysInMonth 31](#_Toc166161583)

[2.51 getAddMonths 32](#_Toc166161584)

[2.52 getStrData 32](#_Toc166161585)

[2.53 getDbTime 33](#_Toc166161586)

[2.54 substrByte 33](#_Toc166161587)

[2.55 parseDate 34](#_Toc166161588)

[2.56 isValidDate 34](#_Toc166161589)

[2.57 toDateString 34](#_Toc166161590)

[2.58 getTextSize 35](#_Toc166161591)

[2.59 getChkRow 35](#_Toc166161592)

[2.60 getFindRows 35](#_Toc166161593)

[2.61 getFindRowsExpr 36](#_Toc166161594)

[2.62 isEmpty 36](#_Toc166161595)

[2.63 getTrim 36](#_Toc166161596)

[2.64 isObject 37](#_Toc166161597)

[2.65 getObjectAssign 37](#_Toc166161598)

[2.66 getFileExt 37](#_Toc166161599)

[2.67 copyDsLayout 38](#_Toc166161600)

[2.68 formCenter 38](#_Toc166161601)

[2.69 getSvcUrl 38](#_Toc166161602)

[2.70 mdiOpenMenu 39](#_Toc166161603)

[2.71 getDate 39](#_Toc166161604)

[2.72 fnGridCheckAll 39](#_Toc166161605)

[2.73 fnStrToObject 40](#_Toc166161606)

[2.74 getUrlParams 40](#_Toc166161607)

[2.75 isMobile 40](#_Toc166161608)

[2.76 tranSave 41](#_Toc166161609)

[2.77 CompList 41](#_Toc166161610)

[2.78 setSystemInfo 42](#_Toc166161611)

[2.79 getParentXY 42](#_Toc166161612)

[2.80 getTreeChildRows 42](#_Toc166161613)

[2.81 getTreeFamilyRows 43](#_Toc166161614)

[2.82 getTreeNodeRows 43](#_Toc166161615)

[2.83 getTreeLevRows 43](#_Toc166161616)

[2.84 getTreeLevelInfo 44](#_Toc166161617)

[2.85 getGridHeadInfo 44](#_Toc166161618)

[2.86 StringToObject 45](#_Toc166161619)

[2.87 CopyObject 45](#_Toc166161620)

[2.88 getCompObjects 45](#_Toc166161621)

[2.89 comBtnRoleAll 46](#_Toc166161622)

[2.90 comBtnRoleOne 46](#_Toc166161623)

[2.91 textLengthOverCut 47](#_Toc166161624)

[2.92 setCookie 47](#_Toc166161625)

[2.93 getCookie 47](#_Toc166161626)

[2.94 getProgInfo 48](#_Toc166161627)

[3\. 공통 JS ProtoType 49](#_Toc166161628)

[3.1 replaceMulti 49](#_Toc166161629)

[3.2 ltrimzero 49](#_Toc166161630)

[3.3 cutbytes 49](#_Toc166161631)

[3.4 lpad 50](#_Toc166161632)

[3.5 rpad 50](#_Toc166161633)

[3.6 rightstr 50](#_Toc166161634)

[3.7 splitEmpty 51](#_Toc166161635)

[3.8 ArrayUnique 51](#_Toc166161636)

[3.9 ArrayTrim 51](#_Toc166161637)

[3.10 ArrayLastindexOfProp 52](#_Toc166161638)

[3.11 ArrayIndexOf 53](#_Toc166161639)

# **1\. Take Java API**

## 1.1 TakeDataRequest.java

### 1.1.1 getParamMap

\- dsSearch 또는 parameter를 Map형태로 조회 (+세션정보)

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     | Map | Nexacro에서 넘겨준 dsSearch,<br><br>parameter를<br><br>Map 형태로 반환 |
| **Example** |     |     |     |     |
| Map&lt;String, Object&gt; params = takeDataRequest.getParamMap(); |     |     |     |     |

### 1.1.2 getMapList

\- DataSet을 List&lt;Map&gt;으로 조회 (+세션정보)

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | datasetId | DataSet ID | List&lt;Map&gt; | Nexacro에서 넘겨준 DataSet을<br><br>List&lt;Map&gt; 형태로 반환 |
| **Example** |     |     |     |     |
| List&lt;Map<String, Object&gt;> list = takeDataRequest. getOriginalMapList("dsList");<br><br>for (Map&lt;String, Object&gt; data : list) {<br><br>DataSetRowStatus rowType = (DataSetRowStatus) data.get(TakeConstants.ROWTYPE);<br><br>if (rowType == DataSetRowStatus.INSERT) {<br><br>takeDAO.insert("Sample01.smpFormInsert", data);<br><br>} else if (rowType == DataSetRowStatus.UPDATE) {<br><br>takeDAO.update("Sample01.smpFormUpdate", data);<br><br>} else if (rowType == DataSetRowStatus.DELETE) {<br><br>takeDAO.delete("Sample01.smpFormDelete", data);<br><br>}<br><br>} |     |     |     |     |

### 1.1.3 getOriginalMapList

\- DataSet을 List&lt;Map&gt;으로 조회

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | datasetId | DataSet ID | List&lt;Map&gt; | Nexacro에서 넘겨준 DataSet을<br><br>세션정보없이 List&lt;Map&gt; 형태로 반환 |
| **Example** |     |     |     |     |
| List&lt;Map<String, Object&gt;> list = takeDataRequest. getOriginalMapList("dsList");<br><br>for (Map&lt;String, Object&gt; data : list) {<br><br>DataSetRowStatus rowType = (DataSetRowStatus) data.get(TakeConstants.ROWTYPE);<br><br>if (rowType == DataSetRowStatus.INSERT) {<br><br>takeDAO.insert("Sample01.smpFormInsert", data);<br><br>} else if (rowType == DataSetRowStatus.UPDATE) {<br><br>takeDAO.update("Sample01.smpFormUpdate", data);<br><br>} else if (rowType == DataSetRowStatus.DELETE) {<br><br>takeDAO.delete("Sample01.smpFormDelete", data);<br><br>}<br><br>} |     |     |     |     |

### 1.1.4 getDataSet

\- TakeDataSet 반환

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | datasetId | DataSet ID | TakeDataSet | Nexacro에서 넘겨준 DataSet 중<br><br>DataSet ID와 일치하는 DataSet 반환 |
| **Example** |     |     |     |     |
| TakeDataSet dsList = takeDataRequest.getDataSet("dsList");<br><br>dsList.forEachRow(new TakeDataSetRowStatusCallback&lt;Map<String, Object&gt;>() {<br><br>@Override<br><br>public void insert(Map&lt;String, Object&gt; record, int rowNum) {<br><br>takeDAO.insert("Sample.dataInsert", record);<br><br>}<br><br>@Override<br><br>public void update(Map&lt;String, Object&gt; newRecord, Map&lt;String, Object&gt; oldRecord, int rowNum) {<br><br>takeDAO.update("Sample.dataUpdate", newRecord);<br><br>}<br><br>@Override<br><br>public void delete(Map&lt;String, Object&gt; record, int rowNum) {<br><br>takeDAO.delete("Sample.dataDelete", record);<br><br>}<br><br>}, LinkedHashMap.class); |     |     |     |     |

### 1.1.5 getDataSetList

\- 모든 TakeDataSet 객체 List 반환

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     | List&lt;TakeDataSet&gt; | Nexacro에서 넘겨준 DataSet List |
| **Example** |     |     |     |     |
| List&lt;TakeDataSet&gt; datasetList = takeDataRequest.getDataSetList(); |     |     |     |     |

### 1.1.6 getDataSets

\- 모든 TakeDataSet Map 반환

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     | Map&lt;String, TakeDataSet&gt; | Nexacro에서 넘겨준 DataSet을<br><br>DataSet ID, TakeDataSet 형태로 반환 |
| **Example** |     |     |     |     |
| Map&lt;String, TakeDataSet&gt; dataSetInfo = takeDataRequest.getDataSets(); |     |     |     |     |

### 1.1.7 getObjectList

\- List&lt;Object&gt; 타입으로 DataSet 반환

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | datasetId | DataSet ID | List&lt;T&gt; | Nexacro에서 넘겨준 DataSet을<br><br>List&lt;T&gt; 형태로 반환 |
| **Example** |     |     |     |     |
| List&lt;BoardInfo&gt; boardList = takeDataRequest.getObjectList("dsBoard", BoardInfo.class); |     |     |     |     |

### 1.1.8 getPrimitiveList

\- Nexacro DataSetList 반환

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     | DataSetList | Nexacro에서 넘겨준 DataSet을<br><br>DataSetList 형태로 반환 |
| **Example** |     |     |     |     |
| DataSetList dsList = takeDataRequest.getPrimitiveList(); |     |     |     |     |

### 1.1.9 getString

\- Nexacro Parameter 반환

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | param | Parameter Name | String | Nexacro에서 넘겨준 dsSearch, parameter를 String 형태로 반환 |
| **Example** |     |     |     |     |
| String title = takeDataRequest.getString("title"); |     |     |     |     |

## 1.2 TakeDataResponse.java

### 1.2.1 addDataSet

\- 응답 DataSet 지정

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | datasetId | DataSet ID |     |     |
| Object | dataset | DataSet |
| **Example** |     |     |     |     |
| List&lt;LinkedHashMap<String, Object&gt;> dsList = service.select(paramMap());<br><br>takeDataResponse.addDataSet("dsList", dsList); |     |     |     |     |

### 1.2.2 addParam

\- 응답 Form Variable 지정

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Map | addParamMap | FormVariables |     |     |
| **Example** |     |     |     |     |
| Map&lt;String, Object&gt; addParamMap = new HashMap<>();<br><br>addParamMap.put("fv_insertCount", 30);<br><br>addParamMap.put("fv_updateCount", 10);<br><br>takeDataResponse.addParam(addParamMap); |     |     |     |     |

### 1.2.3 addParam

\- 응답 Form Variable 지정

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | paramName | FormVariable ID |     |     |
| String | paramValue | FormVariable |
| **Example** |     |     |     |     |
| takeDataResponse.addParam("fv_insertCount", "30"); |     |     |     |     |

### 1.2.4 addPagingDataSet

\- 페이징 처리 된 응답 DataSet 지정

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | datasetId | DataSet ID |     |     |
| Object | dataset | DataSet |     |     |
| Map&lt;String, Object&gt; | pagingParam | 페이징 정보 |     |     |
| **Example** |     |     |     |     |
| List&lt;LinkedHashMap<String, Object&gt;> dsList = service.select(paramMap);<br><br>Map&lt;String, Object&gt; pagingParam = TakePageDTO.of(dsList, paramMap).toMap();<br><br>takeDataResponse.addPagingDataSet("dsPagedList", dsList, pagingParam); |     |     |     |     |

### 1.2.5 success

\- 성공 응답 전송

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     |     |     |
| **Example** |     |     |     |     |
| takeDataResponse.success(); |     |     |     |     |

### 1.2.6 error

\- 오류 응답 전송

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     |     |     |
| **Example** |     |     |     |     |
| takeDataResponse.error(); |     |     |     |     |

### 1.2.7 error

\- 사용자지정 오류 응답 전송

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| int | errorCode | 에러코드 |     |     |
| String | errorMsg | 에러메세지 |
| **Example** |     |     |     |     |
| takeDataResponse.error(-203, "고객 등록 실패"); |     |     |     |     |

### 1.2.8 write

\- 성공 응답 전송

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     |     |     |
| **Example** |     |     |     |     |
| takeDataResponse.write(); |     |     |     |     |

### 1.2.9 write

\- 사용자지정 응답 전송

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| int | errorCode | 에러코드 |     |     |
| String | errorMsg | 에러메세지 |
| **Example** |     |     |     |     |
| takeDataResponse.write(-203, "고객 등록 실패"); |     |     |     |     |

# 2\. Take JS Function 구성

## 2.1 ComponentList

\- 폼 컴포넌트 리스트

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | Form | Array | 컴포넌트 Array |
| **Example** |     |     |     |     |
| Take.ComponentList(this) //--> array \[btnAdd,btnTest\] |     |     |     |     |

## 2.2 isQuickView

\- 퀵뷰 실행 여부 확인.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     | Boolean | true/false |
| **Example** |     |     |     |     |
| take.isQuickView(this) //--> true/false |     |     |     |     |

## 2.3 ObjectPath

\- 컴포넌트 전체 경로 확인.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | obj | 컴포넌트 | String | Path 전체 PATH |
| **Example** |     |     |     |     |
| take.ObjectPath(this) //--> true/false |     |     |     |     |

## 2.4 isNull

\- Null Check.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| \*  | val | 체크할 값 | Boolean | null 여부 |
| **Example** |     |     |     |     |
| take.isNull(this) //--> true/false |     |     |     |     |

## 2.5 isFunction

\- value의 Function 여부 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| \*  | val | 확인할 value | Boolean | Function 여부 |
| **Example** |     |     |     |     |
| trace(take.isFunction(this)) //--> true/false |     |     |     |     |

## 2.6 getTodayTime

\- 날짜 구하기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     | Object | 시스템 타입 반환. desktop, phone, tablet |
| **Description** |     |     |     |     |
| objDateTime<br><br>objDateTime.year 년<br><br>objDateTime.month 월<br><br>objDateTime.day 일<br><br>objDateTime.date 년월일<br><br>objDateTime.hh 시<br><br>objDateTime.mm 분<br><br>objDateTime.ss 초<br><br>objDateTime.time 시분초 |     |     |     |     |

## 2.7 ObjectType

\- 오브젝트의 타입을 String으로 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | obj | 오브젝트 | String | 오브젝트 타입 |
| **Example** |     |     |     |     |
| take.objectType(this) //--> Form |     |     |     |     |

## 2.8 CompTypeName

\- 컴포넌트 타입을 문자열로 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objComp | 컴포넌트 | String | 컴포넌트 타입명 |
| **Example** |     |     |     |     |
| take.compTypeName(this) //--> Form |     |     |     |     |

## 2.9 CompType

\- 컴포넌트 유형 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     | Object |     |
| **Description** |     |     |     |     |
| objRtn<br><br>objRtn.type {String} 컴포넌트 타입<br><br>objRtn.comp {Component Object} 컴포넌트 오브젝트 |     |     |     |     |

## 2.10 setComma

\- 숫자 또는 문자에 콤마 표시.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String, Number | data | 숫자인 문자형 또는 숫자형 | String | 콤마가 표시된 값 |
| **Example** |     |     |     |     |
| take.setComma(123456.12); // --> 123,456.12 |     |     |     |     |

## 2.11 getByteLength

\- 문자열의 byte 길이를 반환한다. 한글의 경우 "utf-8"로 인코딩되면 3 bytes로 처리한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String/Number | sVal | 체크할 문자열 | Number |     |
| String | sCharset | 인코딩 \[default utf-8\] |
| **Example** |     |     |     |     |
| take.getByteLength("1234"); // --> 4 |     |     |     |     |

## 2.12 isEmail

\- 이메일 형식 확인.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sEmail | 이메일 | Boolean | 값이 존재할 경우에 체크 |
| **Example** |     |     |     |     |
| take.isEmail("aaa.test.com"); //--> true/false |     |     |     |     |

## 2.13 isDate

\- Date 형식 확인.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sValue | 날짜  | Boolean | true / false |
| **Example** |     |     |     |     |
| take.isDate("20180328") //--> true/false |     |     |     |     |

## 2.14 isFromTo

\- 시작일과 종료일을 체크 한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sFDate | 시작일자 | Boolean | true/false |
| String | sTDate | 종료일자 |
| **Example** |     |     |     |     |
| take.isFromTo("20150101", "20150101"); // --> true/false |     |     |     |     |

## 2.15 replaceFormat

\- 문자열에서 포맷된 부분을 파라메타로 치환한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String, Number |     | 포멧 문자열 |     | 변환된 문자열 |
| **Example** |     |     |     |     |
| trace( take.replaceFormat("Hello {0}!", "take")); -> "Hello teke!"<br><br>trace( take.replaceFormat("Hello {0}!{1}!", "take", "test")); -> "Hello take!test!"<br><br>trace( take.replaceFormat("{} Hello {}!", "take", "test")); -> "take Hello test!" |     |     |     |     |

## 2.16 decode

\- 디코딩.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String, Number |     | decode 조건값 |     | decode 결과값 |
| **Example** |     |     |     |     |
| trace(take.decode("1", "1", "One", "2", "Two", "Default")); // --> output : One<br><br>trace(take.decode(100, 1, "일", 10, "십", 100, "백")); // --> output : 백 |     |     |     |     |

## 2.17 getUniqueId

\- 유일한 ID를 반환한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | prefix | id 앞에 붙일 문자열 | String |     |
| String | separator | id 생성시 구분용 문자(default: '-' ) |
| **Example** |     |     |     |     |
| trace(take.getUniqueId()); // output : 3e52d1f6-f0d2-4970-a590-ba7656b07859<br><br>trace(take.getUniqueId("Button_"));<br><br>// output : Button_4e601da1-63f4-4cfa-849b-01b8a7f14d40<br><br>trace(take.getUniqueId("", "\_")); // output : 4e601da1_63f4_4cfa_849b_01b8a7f14d40<br><br>trace(take.getUniqueId("Button_", "\_"));<br><br>// output : Button_4e601da1_63f4_4cfa_849b_01b8a7f14d40 |     |     |     |     |

## 2.18 getSequenceId

\- Form 내에서 지정된 접두문자열에 순번이 붙여진 ID 를 반환한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | form | 순번 앞에 붙일 문자열 | String |     |
| String | prefix |
| **Example** |     |     |     |     |
| trace(take.getSequenceId(this, "Button")); // output : Button0<br><br>trace(take.getSequenceId(this, "Button")); // output : Button1<br><br>trace(take.getSequenceId(this, "chk_")); // output : chk_0<br><br>trace(take.getSequenceId(this, "chk_")); // output : chk_1 |     |     |     |     |

## 2.19 ArrayPluck

\- 배열의 특정 위치의 값을 추출한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Array | arrData | 배열  | Array |     |
| Number | key | 추출할 배열Index |
| **Example** |     |     |     |     |
| arrData = new Array();<br><br>take.ArrayPluck(arrData, 1); |     |     |     |     |

## 2.20 getTextlimitTo

\- 텍스트의 길이수를 체크하여 "..."반환

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sText | 변환할 텍스트 | String |     |
| Anonymous | aFont | 폰트  |
| Number | nLimitSize | 제한 사이즈 |
| **Example** |     |     |     |     |
| take.getTextlimitTo("텍스트", "11px Gulim", 20); //텍... |     |     |     |     |

## 2.21 getFunctionName

\- 폼에서 정의한 사용자 함수의 이름 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | nexacro form object | String | 함수명 |
| **Example** |     |     |     |     |
| take.getFunctionName(this) |     |     |     |     |

## 2.22 debug

\- debug를 출력한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object/String | pThis | Form Object 또는 시스템 아이디 |     |     |
| String | sMsg | 디버그 메세지 |
| **Example** |     |     |     |     |
| take.debug(this, "디버그입니다."); |     |     |     |     |

## 2.23 error

\- error log를 출력한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object/String | pThis | Form Object 또는 시스템 아이디 |     |     |
| String | sMsg | 에러 메세지 |
| **Example** |     |     |     |     |
| take.debug(this, "에러입니다."); |     |     |     |     |

## 2.24 trace

\- Trace를 찍는다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sId | 시스템 아이디 |     |     |
| String | sGbn | 구분  |
| String | sMsg | 메시지 |
| **Example** |     |     |     |     |
| take.trace("System", "ERROR", "메세지입니다."); |     |     |     |     |

## 2.25 alert

\- 공통 Alert Error시에만 별도 로직이 추가된다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | 폼 오브젝트 |     |     |
| String | sType | 메세지 타입 (Error, Info, Warning등) |
| String | sMsgId | 다국어 메세지 ID |
| Array | arrParam | 파라메터 |
| **Example** |     |     |     |     |
| take.alert(this, "Info", "ML001", { name : "test", text : "정의"});<br><br>take.alert(this, "Info", "{name}가 {text}되지 않았습니다.", { name : "test", text : "정의"}); |     |     |     |     |

## 2.26 confirm

\- 공통 Confirm.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | 폼 오브젝트 |     |     |
| String | sType | 컨펌 타입 ("error", "question", "warning", "information") |
| String | sMsgId | 다국어 메세지 ID |
| Array | arrParam | 파라메터 |
| **Example** |     |     |     |     |
| take.confirm(this, "question", "ML001", { name : "test", text : "정의"});<br><br>take.confirm(this, "question", "{name}가 {text}되지 않았습니다.", { name : "test", text : "정의"}); |     |     |     |     |

## 2.27 setLocalData

\- 로컬스토리지에 데이터셋을 저장

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Dataset Object | objDs | 로컬스토리에 저장할 데이터셋 | boolean | 성공/실패 여부 |
| **Example** |     |     |     |     |
| take.setLocalData(this.dsData); --> true/false |     |     |     |     |

## 2.28 getLocalData

\- 로컬스토리지에 데이터셋을 저장

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Dataset Object | objDs | 로컬스토리에 저장할 데이터셋 | boolean | 성공/실패 여부 |
| **Example** |     |     |     |     |
| take.getLocalData(this.dsData); --> true/false |     |     |     |     |

## 2.29 getBindColName

\- body cell index로 binding 된 컬럼명을 얻어온다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objGrid | Grid Component | String | 컬럼아이디 |
| Number | nIdx | Grid body Cell index |
| **Example** |     |     |     |     |
| take.getBindColName(this.Grid00, 1); |     |     |     |     |

## 2.30 formOnLoad

\- 공통 Onload.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | nexacro Form Object | boolean | true/false 여부 |
| Boolean | bGrid | 그리드 기능 사용여부 |
| **Example** |     |     |     |     |
| trace(take.formOnLoad(this)); //--> true |     |     |     |     |

## 2.31 formRole

\- 공통 Onload.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | nexacro Form Object | boolean | true/false 여부 |
| **Example** |     |     |     |     |
| trace(take.formRole(this)); //--> true |     |     |     |     |

## 2.32 svcFindReplace

\- 현재 화면이 실행되는 URL을 확인하여 svcid를 바꾼다

## 2.33 transaction

\- 공통 트랜젝션.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | nexacro form object | Function | CallBack Function |
| String | sTranId | 서비스아이디 |
| String | sUrl | 서비스 URL |
| String | sInDs | 서버로 보낼 데이터셋 |
| String | sOutDs | 서버에서 받을 데이터셋 |
| String | sParam | 파라메터 |
| String | sCallBack | 트랜젝션 완료후 실행할 CallBack 함수 |
| boolen | bAsync |     |
| **Example** |     |     |     |     |
| take.transaction(this, "test", "http://localhost/test.jsp", "", "", "", "fnCallBack", true); |     |     |     |     |

## 2.34 tranCallBack

\- 공통 콜백.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sId | 서비스 아이디 |     |     |
| Number | nErrCd | 에러코드 0보다 작을 경우 에러 |
| String | sErrMsg | 에러메세지 |
| **Example** |     |     |     |     |
| Trace.tranCallBack("test", "error"); |     |     |     |     |

## 2.35 tranSelect

\- 데이터 Select

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | nexacro form object |     |     |
| String | sNameSpace | nexup Name Space |
| String | sInDs | Server에 보낼 데이터셋 명 (여러건일 경우 ','를 기본 구분자로 사용) |
| String | sOutDs | UI에서 받을 데이터셋 명 (데이터셋명이 없을경우 json으로 처리) |
| String | sParam | 파라메터 |
| String | sCallBack | 트랜젝션 콜백 함수 명 |
| boolen | bAsync |     |
| **Example** |     |     |     |     |
| take.fnTranSelect(this, "Select", "Sample.dashSample", "", "dsSample", "", "fnCallback", true); |     |     |     |     |

## 2.36 tranCode

\- 코드 데이터 Select.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | Form Object |     |     |
| String | sGroupCode | 코드 그룹코드 |
| String | sOutDs | UI에서 받을 데이터셋 명 |
| String | sCallBack | UI Transaction Call Back 함수명 |
| **Example** |     |     |     |     |
| take.fnTranCode(this, "000001", "dsCode", "fnCallback"); |     |     |     |     |

## 2.37 openPopup

\- 팝업 오픈

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | Form Object |     | 팝업  |
| String | sFrameId | 프레임 아이디 |
| String | sFormUrl | Form URL |
| Object | objArgList | 팝업에 넘길 인자값 |
| String | sOptions | 옵션  |
| String | sPopupCallback | 콜백 함수 |
| boolen | bModeless | 모달리스 여부 |
| **Example** |     |     |     |     |
| take.openPopup(this, "PopUp", "sample::samplePop.xfdl", {param1: "param1"}, "showtitlebar=false layered=true", "fnCallBack", false); |     |     |     |     |

## 2.38 dataSelPopUp

\- 공통 데이터 팝업

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | Form Object | Function | CallBack Function |
| String | sPopId | 팝업아이디 |
| String | sTitle | 팝업타이틀 |
| String | sTxt | 검색어 |
| Object | objDs | 데이터셋 |
| String | sNameSapce | 네임스페이스 |
| Object | objDsIn | 검색조건 데이터셋 |
| Array | arrColInfo | 대상 컬럼 (컬럼id, 컬럼명, 컬럼 사이즈) |
| boolen | bMulti | 멀티 선택 여부 |
| String | sCallBack | 완료후 실행할 CallBack 함수 |
| **Example** |     |     |     |     |
| take.dataSelPopUp(this, "test", "테스트팝업", "테스트", this.dsCode, "", null, \[\["Column1", "컬럼이번", "30"\],\["Column0", "컬럼일번", "20"\]\], true, "fnCallBack"); |     |     |     |     |

## 2.39 nvl

\- empty값인 경우 대체 값으로 치환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| \*  | Val | 치환대상 | String | 치환값 |
| \*  | rtnValue | 치환값 |
| **Example** |     |     |     |     |
| take.nvl(Val, rtnValue); |     |     |     |     |

## 2.40 isNumber

\- 숫자 여부 확인.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| anonymous | aVal | 확인 대상 값 | boolean | 숫자 여부 |
| **Example** |     |     |     |     |
| take.isNumber(aVal); //--> true / false |     |     |     |     |

## 2.41 getUser

\- User 정보 가져오기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sCol | 컬럼명 | String | sCol 컬럼값 |
| **Example** |     |     |     |     |
| take.getUser(sCol); |     |     |     |     |

## 2.42 isStudio

\- 현재 실행 중인 환경이 개발 툴인지 여부를 확인한다.

## 2.43 getOwnerForm

\- 최상위 폼 찾기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objComp | obj 컴포넌트 | Function | object Form |
| **Example** |     |     |     |     |
| take.getOwnerForm(objComp); |     |     |     |     |

## 2.44 getActiveForm

\- 현재 선택된 탭의 폼 찾기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objComp | obj 컴포넌트 | Function | object Form |
| **Example** |     |     |     |     |
| take.getActiveForm(objComp); |     |     |     |     |

## 2.45 getParentForm

\- 부모 폼 찾기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objComp | obj 컴포넌트 | Function | object Form |
| **Example** |     |     |     |     |
| take.getParentForm(objComp); |     |     |     |     |

## 2.46 getConvertDate

\- 날자 형식을 Object로 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Anonymous | aDate | 날짜  | Object | 날자형 오브젝트 반환 |
| **Example** |     |     |     |     |
| take.getConvertDate(aDate); // Failed -> null 반환 |     |     |     |     |

## 2.47 getDateWeek

\- 요일 구하기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objDate | 날짜  | String | '일', '월', '화', '수', '목', '금', '토' |
| Boolean | bKor |     |
| **Example** |     |     |     |     |
| take.getDateWeek("20180101"); |     |     |     |     |

## 2.48 getDateTerm

\- 두개의 날자 기간 일로 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Anonymous | aSDate | aSDate 날짜 1 | Number | 일수  |
| Anonymous | aEDate | aEDate 날짜 2 |
| **Example** |     |     |     |     |
| take.getDateTerm("20180101","20180131"); |     |     |     |     |

## 2.49 isLeapYear

\- 윤년여부.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Number | aDate | 년도  | Boolean | true/false |
| **Example** |     |     |     |     |
| take.isLeapYear(2010); |     |     |     |     |

## 2.50 getDaysInMonth

\- 해당 월의 마지막 날 리턴.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Number | nYear | 년도  | Number | 마지막 일자 |
| Number | nMonth | 월   |
| **Example** |     |     |     |     |
| take.getDaysInMonth(2010,1); |     |     |     |     |

## 2.51 getAddMonths

\- 월 더하기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Anonymous | aDate | Date | Number | 월을 더한 date |
| Number | nVal | 더할 수 |
| **Example** |     |     |     |     |
| take.getAddMonths("20180101",1); |     |     |     |     |

## 2.52 getStrData

\- 날짜 구하기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     | Object | 시스템 타입 반환. desktop, phone, tablet |
| **Description** |     |     |     |     |
| objDateTime<br><br>objDateTime.year 년<br><br>objDateTime.month 월<br><br>objDateTime.day 일<br><br>objDateTime.date 년월일 |     |     |     |     |

## 2.53 getDbTime

\- 날짜 구하기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     | Object | 시스템 타입 반환. desktop, phone, tablet |
| **Description** |     |     |     |     |
| objDateTime<br><br>objDateTime.year 년<br><br>objDateTime.month 월<br><br>objDateTime.day 일<br><br>objDateTime.date 년월일<br><br>objDateTime.hh 시<br><br>objDateTime.mm 분<br><br>objDateTime.ss 초<br><br>objDateTime.time 시분초 |     |     |     |     |

## 2.54 substrByte

\- 문자열을 바이트로 substring 한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sVal | 문자열 | String |     |
| Number | nStart | 시작위치 |
| Number | nLength | 길이  |
| String | sUnit | 인코딩 값 utf8,ascii 만 가능 |
| **Example** |     |     |     |     |
| take.substrByte("1234",0,4); // --> 1234 |     |     |     |     |

## 2.55 parseDate

\- 날짜(시간)를 파싱해서 DateTime 객체를 생성

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sDate | 일자  | DateTime | 데이터 객체 실패시 null |
| Number | sFormat | 데이터 포멧 |
| **Example** |     |     |     |     |
| take.parseDate("20150101", "yyyyMMdd") |     |     |     |     |

## 2.56 isValidDate

\- 날짜포멧이 맞는지 체크한다

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sDate | 일자  | Boolean |     |
| Number | sFormat | 데이터 포멧 |
| **Example** |     |     |     |     |
| take.isValidDate("20150101", "yyyyMMdd") |     |     |     |     |

## 2.57 toDateString

\- DateTime 객체를 지정된 날짜(시간) 포맷 문자열로 변환한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | dtValue | 일자  | String |     |
| Number | sFormat | 데이터 포멧 |
| **Example** |     |     |     |     |
| take.toDateString(datetime, "yyyyMMdd") |     |     |     |     |

## 2.58 getTextSize

\- 텍스트 사이즈를 구한다.

## 2.59 getChkRow

\- 체크박스(CHK컬럼)가 체크된 Row를 배열로 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objDs | Dataset | Array | 컬럼아이디 |
| String | sChkCol | 체크컬럼명 (CHK) |
| **Example** |     |     |     |     |
| take.getChkRow(this.dsList); |     |     |     |     |

## 2.60 getFindRows

\- 데이터 셋의 해당 컬럼에 일치하는 Row를 배열로 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objDs | Dataset | Array | 일치하는 Row를 배열로 반환 |
| String | aCol | 컬럼명 / 컬럼 index |
| String | sVal | 찾을 값 |
| boolean | bFilter | 필터링 기준으로 처리 여부 (기본값 false) |
| **Example** |     |     |     |     |
| take.getChkRow(this.dsList); |     |     |     |     |

## 2.61 getFindRowsExpr

\- 데이터 셋의 해당 컬럼에 일치하는 Row를 배열로 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objDs | Dataset | Array | 일치하는 Row를 배열로 반환 |
| String | sExpr | Expr |
| boolean | bFilter | 필터링 기준으로 처리 여부 (기본값 false) |
| **Example** |     |     |     |     |
| take.getFindRowsExpr(this.dsList, "COLUMN00=='01', false); |     |     |     |     |

## 2.62 isEmpty

\- Empty 체크.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sValue | 값   | Boolean | Empty 여부 |
| **Example** |     |     |     |     |
| take.isEmpty("test"); //--> true |     |     |     |     |

## 2.63 getTrim

\- null 체크후 trim

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sValue | 값   | String | trim된 값 |
| **Example** |     |     |     |     |
| take.getTrim("te st"); //--> test |     |     |     |     |

## 2.64 isObject

\- Object 체크

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sValue | 값   | Boolean | Object 여부 |
| **Example** |     |     |     |     |
| take.isObject(objTest); //--> true |     |     |     |     |

## 2.65 getObjectAssign

\- Object를 합쳐서 리턴

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objMain | 리턴할 Object | Object | 합쳐진 Object |
| Object | objCopy | 복사할 Object |
| **Example** |     |     |     |     |
| take.getFileExt("C:\\\\abcd.exe"); //--> exe |     |     |     |     |

## 2.66 getFileExt

\- 파일 확장자 확인

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sFileName | 파일 네임(풀) | String | 확장자 |
| **Example** |     |     |     |     |
| take.getFileExt("C:\\\\abcd.exe"); //--> exe |     |     |     |     |

## 2.67 copyDsLayout

\- 데이타셋 스키마정보를 복사.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objRtnDs | 대상(리턴할) 데이터셋 | Object(Dataset) | 리턴 데이터셋 |
| Object | objCopyDs | 카피할 데이터셋 |
| **Example** |     |     |     |     |
| take.gf_copyLayout(Dataset00, Dataset01); //--> Dataset00 |     |     |     |     |

## 2.68 formCenter

\- 컴포넌트를 폼에 중앙 정렬(Width).

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objComp | Object | Array | 성공 실패 여부반환 |
| Number | nFormWidth | Form Width |
| Number | nMinWidth | 최소 Width |
| **Example** |     |     |     |     |
| take.formCenter(this.div, 500, 300); |     |     |     |     |

## 2.69 getSvcUrl

\- 현재 서비스하고 있는 URL을 구한다.

## 2.70 mdiOpenMenu

\- MDI창 오픈

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Form Object | pThis | 대상 폼 |     |     |
| String | sMenuId | 메뉴아이디 |
| String | sParam | 파라메터 |
| String | sCallFunc | 콜백 함수 |
| **Example** |     |     |     |     |
| take.mdiOpenMenu(this, "MI2030", "test\|test1\|test2", "fnTest"); |     |     |     |     |

## 2.71 getDate

\- 날짜 조회

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pOption | {baseDate:yyyyMMdd, addYear:int, addMonth:int, addDate:int} | Object | {year:yyyy, month:MM, day:dd, date:yyyyMMdd} |
| **Example** |     |     |     |     |
| take.getDate(pOption) |     |     |     |     |

## 2.72 fnGridCheckAll

\- 전체클릭 기능 실행

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| obj:nexacro.Grid |     | Grid |     |     |
| e:.GridClickEventInfo |     |     |
| pColId |     | ColId |
| **Example** |     |     |     |     |
| take.fnGridCheckAll(pObj, pGridClickEventInfoCell, pColId) |     |     |     |     |

## 2.73 fnStrToObject

\- 문자열을 Object로 변환 ("k1:v1|k2:v2|k3:v3" => {k1:v1,k2:v2,k3:v3})

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pObjStr |     | Object |     |
| **Example** |     |     |     |     |
| take.fnStrToObject(pObjStr); |     |     |     |     |

## 2.74 getUrlParams

\- Url에서 파라메터 축출후 리턴

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | Url |     | Object | 파라메터 Object |
| **Example** |     |     |     |     |
| take.getUrlParams("http://www.test.co.kr/?test=1") |     |     |     |     |

## 2.75 isMobile

\- 모바일 / PC 여부 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     | boolean | Function 여부 |
| **Example** |     |     |     |     |
| take.isMobile(); |     |     |     |     |

## 2.76 tranSave

\- 데이터 Save

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | nexacro form object |     |     |
| String | sNameSpace | nexup Name Space |
| String | sInDs | Server에 보낼 데이터셋 명 (여러건일 경우 ','를 기본 구분자로 사용) |
| String | sOutDs | UI에서 받을 데이터셋 명 (데이터셋명이 없을경우 json으로 처리) |
| String | sParam | 파라메터 |
| String | sCallBack | 트랜젝션 콜백 함수 명 |
| **Example** |     |     |     |     |
| take.fnTranSave(this, "Save", "Sample.dash2", "dsSample", "", "", "fnCallback"); |     |     |     |     |

## 2.77 CompList

\- 컴포넌트 리스트 가져오기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objForm | From Object | Array | 배열값(컴포넌트 정보) |
| **Example** |     |     |     |     |
| take.CompList(this) //--> Grid00.0\|순번,Grid00.1\|선택,Div.Static00\|검색조건,Button00\|조회 |     |     |     |     |

## 2.78 setSystemInfo

\- 시스템 기본 정보 세팅.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objSys | 시스템 정보 | Boolean | 성공/실패 |
| **Example** |     |     |     |     |
| take.setSystemInfo(objSys) |     |     |     |     |

## 2.79 getParentXY

\- 부모 폼에서 내 x, y 찾기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | obj | 컴포넌트 | object | \[X,Y\] |
| Boolean | bCallee | True / false |
| Number | nX  | X 축 |
| Number | nY  | Y 축 |
| **Example** |     |     |     |     |
| take.getParentXY(objComp, bCallee, nX, nY) |     |     |     |     |

## 2.80 getTreeChildRows

\- 트리 컬럼의 자식 노드를 배열로 리턴.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objGrid | Grid Component | Array | Dataset Rows 해당하는 자식 노드 배열 |
| Number | nIdx | Grid body Tree Cell index |
| Number | nRow | Grid body Tree Row index |
| **Example** |     |     |     |     |
| take.getTreeChildRows(objGrid, nIdx, nRow) |     |     |     |     |

## 2.81 getTreeFamilyRows

\- 트리 컬럼의 하위 자손들의 노드를 배열로 리턴.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objGrid | Grid Component | Array | Dataset Rows 해당하는 자식 노드 배열 |
| Number | nIdx | Grid body Tree Cell index |
| Number | nRow | Grid body Tree Row index |
| Boolean | bCallee | 재귀호출여부 사용자 호출시 제외 |
| **Example** |     |     |     |     |
| take.getTreeFamilyRows(this.Grid00, 1, 1); |     |     |     |     |

## 2.82 getTreeNodeRows

\- 트리 컬럼의 자식 노드를 배열로 리턴.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objGrid | Grid Component | Array | Dataset Rows 해당하는 형재 노드 배열 |
| Number | nIdx | Grid body Tree Cell index |
| Number | nRow | Grid body Tree Row index |
| **Example** |     |     |     |     |
| take.getBindColName(this.Grid00, 1, 1); |     |     |     |     |

## 2.83 getTreeLevRows

\- 해당하는 레벨의 노드를 배열로 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objGrid | Grid Component | Array | Dataset Rows 해당하는 노드 배열 |
| Number | nIdx | Grid body Tree Cell index |
| Number | nRow | Grid body Tree Row index |
| **Example** |     |     |     |     |
| take.getTreeLevRows(objGrid, 1, 1); |     |     |     |     |

## 2.84 getTreeLevelInfo

\- 해당하는 레벨의 노드를 배열로 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objGrid | Grid Component | Object | min 최소, max 최대 레벨 값을 Object로리턴 |
| Number | nIdx | tree 컬럼 인덱스 |
| **Example** |     |     |     |     |
| take.getTreeLevelInfo(objGrid, 1); |     |     |     |     |

## 2.85 getGridHeadInfo

\- Grid Head 정보.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objGrid | Grid Component | Object | cellcount : Head 셀 수, rowcount : head 로우 수, height : Head 높이 합을 Object로리턴 |
| **Example** |     |     |     |     |
| take.getGridHeadInfo(objGrid); |     |     |     |     |

## 2.86 StringToObject

\- 문자형 Object를 Object로 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sObj | 문자형 Object {key0:value0, "key1":"value1"...} | Object | Object |
| **Example** |     |     |     |     |
| take.StringToObject("{key0:value0, 'key1':'value1', key2:'value2'}"); |     |     |     |     |

## 2.87 CopyObject

\- 문자형 Object를 Object로 반환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objVal | 문자형 Object {key0:value0, "key1":"value1"...} | Object | 복사한 Object |
| Object | objRtn | 리턴 받을 Object (리턴받을 Object가 있을경우 Add) |
| **Example** |     |     |     |     |
| take.CopyObject({key0:value0, 'key1':'value1', key2:'value2'}); |     |     |     |     |

## 2.88 getCompObjects

\- 타입별 컴포넌트 리스트 가져오기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | objForm | From Object | Object | 배열값(컴포넌트 정보) |
| **Example** |     |     |     |     |
| take.CompList(this) //--> Grid00.0\|순번,Grid00.1\|선택,Div.Static00\|검색조건,Button00\|조회; |     |     |     |     |

## 2.89 comBtnRoleAll

\- 버튼 롤 세팅.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | 대상 폼 | Boolean | true:성공/false:실패 |
| String | sBtnRole | 버튼 권한 6자리 'YYYYNN' 등록,조회,수정,삭제,엑셀,출력 |
| **Example** |     |     |     |     |
| take.comBtnRole(this, "YYYYNN"); |     |     |     |     |

## 2.90 comBtnRoleOne

\- 버튼 롤 세팅.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | pThis | 대상 폼 | Boolean | true:성공/false:실패 |
| String | sBtnId | 버튼 아이디 (등록:Add,조회:Search,수정:Save,삭제:Del,엑셀:Excel,출력:Report) |
| Boolean | bRole | 권한 여부 |
| **Example** |     |     |     |     |
| take.comBtnRoleOne(this, "Excel", true); |     |     |     |     |

## 2.91 textLengthOverCut

\- take textLengthOverCut 문자열을 특정 길이만큼 자르고 대체 문자열을 이어 붙힌다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | sText | 원본 문자열 | String | 문자열 |
| Number | nCnt | 문자열 최대 길이 수 |
| String | sVal | 대체 문자열 |
| **Example** |     |     |     |     |
| take.comBtnRoleOne(this, "Excel", true); |     |     |     |     |

## 2.92 setCookie

\- 쿠키 설정.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     | name |     |     |     |
|     | value |     |
|     | expiredays |     |
| **Example** |     |     |     |     |
| take.setCookie( name, value, expiredays ); |     |     |     |     |

## 2.93 getCookie

\- 쿠키 불러오기.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     | name |     |     |     |
| **Example** |     |     |     |     |
| take.getCookie( name); |     |     |     |     |

## 2.94 getProgInfo

\- MDI 프로그램 정보

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Object | str | nexacro Form | Object | (ProgId, ProgNm) |
| **Example** |     |     |     |     |
| take.getProgInfo(str); |     |     |     |     |

# 3\. 공통 JS ProtoType

## 3.1 replaceMulti

\- n개 이상의 데이터를 변환.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| object | hash | 변환 대상 | String | 변환한 값 |
| **Example** |     |     |     |     |
| sTxt = ' &lt;Form id="{Form_Id}" left="0" top="0" width="{Form_Width}" height="{Form_Height}" titletext="{Form_Title}"&gt;';<br><br>sTxt.replaceMulti({ Form_Id: "test", Form_Title: "테스트", Form_Width: "100", Form_Height: "200"})<br><br>trace("결과 ==> " + sTxt); // 결과 ==> &lt;Form id="test" left="0" top="0" width="100" height="200" titletext="테스트"&gt; |     |     |     |     |

## 3.2 ltrimzero

\- 문자형 숫자에서 '0'을 제거

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
|     |     |     | String | '0'이 제거된 값 |
| **Example** |     |     |     |     |
| trace("001234".ltrimzero()); //--> 1234 |     |     |     |     |

## 3.3 cutbytes

\- 문자열에서 nByte만큼 잘라서 반환한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Number | nByteLen | 문자열 | String |     |
| **Example** |     |     |     |     |
| trace("안녕하세요".cutbytes(4)); --> "안녕..." |     |     |     |     |

## 3.4 lpad

\- 왼쪽에 특정 문자를 채운다. (채울 자리수-현재 자리수 만큼 채운다 ).

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Number | nlan | 채울 자리수 | String | 채운값 |
| String | sChar | 채울 문자 |
| **Example** |     |     |     |     |
| trace("123".lpad(6,"0")); //--> 000123 |     |     |     |     |

## 3.5 rpad

\- 오쪽에 특정 문자를 채운다. (채울 자리수-현재 자리수 만큼 채운다 ).

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Number | nlan | 채울 자리수 | String | 채운값 |
| String | sChar | 채울 문자 |
| **Example** |     |     |     |     |
| trace("123".rpad(6,"0")); //--> 000123 |     |     |     |     |

## 3.6 rightstr

\- Right로 String을 잘라서 반환한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Number | nSize | 자릿수 | String | 리턴값 |
| **Example** |     |     |     |     |
| trace("123456".rightstr(3)); //--> 456 |     |     |     |     |

## 3.7 splitEmpty

\- 문자열을 나누어 배열로 리턴한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| String | str | 구분자 | Array | 문자열을 나눈 배열 |
| **Example** |     |     |     |     |
| string.splitEmpty() |     |     |     |     |

## 3.8 ArrayUnique

\- 배열에 중복제거

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Array | arrData | 배열  | Array | 중복 제거된 배열 |
| **Example** |     |     |     |     |
| arrData = \["a", "b", "b", "c"\]<br><br>take.ArrayUnique(arrData); //--> a,b,c |     |     |     |     |

## 3.9 ArrayTrim

\- 배열에 빈값 제거

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Array | arrData | 배열  | Array | 진값 제거된 배열 |
| **Example** |     |     |     |     |
| arrData = \["a", "", "", "c"\];<br><br>take.ArrayTrim(arrData); //--> a,c |     |     |     |     |

## 3.10 ArrayLastindexOfProp

\- 지정된 속성의 값이 처음으로 일치하는 객체의 배열 위치를 뒤에서부터 찾아 반환한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Array | arrData | 배열  | Number | 검색된 배열 위치. 없다면 -1 리턴. |
| String | prop | 기준 속성 |
| String | item | 기준 값 |
| Number | from | 검색 시작 위치(default: 0) |
| Boolean | strict | true: 형변환 없이 비교('==='), false: 형변환 후 비교('==') (default: false). |
| **Example** |     |     |     |     |
| var users = \[\];<br><br>users\[0\] = {id:"milk", name:"park", age:33};<br><br>users\[1\] = {id:"apple", name:"kim"};<br><br>users\[2\] = {id:"oops", name:"joo", age:44};<br><br>users\[3\] = {id:"beans", name:"lee", age:50};<br><br>users\[4\] = {id:"zoo", age:65};<br><br>users\[5\] = {id:"milk", name:"", age:33};<br><br>users\[6\] = {id:"milk", name:"lee", age:33};<br><br>var index = users.("name", "lee");<br><br>trace("index==>" + index); // output : index==>6<br><br>var index = users.("name", "lee", 5);<br><br>trace("index==>" + index); // output : index==>3 |     |     |     |     |

## 3.11 ArrayIndexOf

\- 지정된 항목이 처음 나오는 배열 위치를 반환한다.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Parameter Type** | **Parameter** | **Param설명** | **Return Type** | **Return설명** |
| Array | arrData | 배열  | Number | 검색된 배열 위치. 없다면 -1 리턴. |
| Object | item | 찾고자 하는 Item. |
| Number | from | from 검색의 시작 위치 (default: 0) |
| Boolean | strict | true: 형변환 없이 비교('==='), false: 형변환 후 비교('==') (default: false). |
| **Example** |     |     |     |     |
| var mon = \["Jan","Feb","Mar","Apr"\];<br><br>var index = mon.getIndexOf("Mar"); // trace("index==>" + index); // output : index==>2<br><br>var index = mon.getIndexOf("May"); // trace("index==>" + index); // output : index==>-1 |     |     |     |     |