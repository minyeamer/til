# Web Crawling
  1. [Web Crawling vs Web Scraping](#1-web-crawling-vs-web-scraping)
  2. [HTML Tags](#2-html-tags)
  3. [The Process of Web Scraping](#3-the-process-of-web-scraping)
  4. [The Process of Data Analysis for Text Data](#4-the-process-of-data-analysis-for-text-data)
  5. [TF-IDF](#5-tf-idf)
     + [Count Vectorizer](#count-vectorizer)
     + [TF-IDF Vectorizer](#tf-idf-vectorizer)
     + [Cosine Similarity](#cosine-similarity)
  6. [Embedding](#6-embedding)

---

## 1. Web Crawling vs Web Scraping
- Web Crawling: Bot이 web을 link를 통해 돌아다니는 것
- Web Scraping: Webpage에서 원하는 자료를 긇어오는 것

---

## 2. HTML Tags
- Tag's Name: `html`, `head`, `body`, `p`, `span`, `li`, `ol`, `ul`, `div`
- Tag's Attribute: `class`, `id`, `style`, `href`, `src`

---

## 3. The Process of Web Scraping
1. URL 분석 (query 종류 등)
2. URL 구성
3. HTTP Response 얻기 (`urlopen(URL)` or `request.get(URL).content`)
4. HTTP source 얻기 (`BeautifulSoup(HTTP Response, 'html.parser')`)
5. HTML Tag 꺼내기 (`.find('tag_name', {'attr_name':'attr_value'})`)
6. Tag로부터 텍스트 혹은 Attribute values 꺼내기 (`Tag.get_text()` or `Tag.attrs`)

---

## 4. The Process of Data Analysis for Text Data
1. 텍스트 데이터를 str 자료형으로 준비
2. Tokenize (형태소 분석)
3. POS Tagging (Part-of-speech, 품사 표시)
4. Stopwords 제거 (불용어 제거)
5. 단어 갯수 카운팅 & 단어 사전 생성
6. 단어 사전 기반 데이터 시각화
7. (+ 머신러닝/딥러닝 모델 적용)

---

## 5. TF-IDF
- Term Frequency - Inverse Document Frequency
- 특정 단어가 문서에서 어떤 중요도를 가지는지를 나타내는 지표
- 많은 문서에 공통적으로 들어있는 단어는 문서 구별 능력이 떨어진다 판단하여 가중치 축소

### Count Vectorizer
- 단어의 빈도수만을 사용해서 벡터 생성

|Document|That|Nice|Car|John|Has|Red|
|:------:|:--:|:--:|:-:|:--:|:-:|:-:|
|A|1|1|1|0|0|0|
|B|1|0|1|1|1|1|

### TF-IDF Vectorizer
- 단어의 빈도수(TF)를 TF-IDF 값으로 변경하여 가중치가 조정된 벡터 생성

![tf-idf_fomular](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FXv4ZI%2FbtrxivVgkVU%2F3y6GQoVIwFimbiKm4pl1f0%2Fimg.png)

### Cosine Similarity
- 두 벡터 사이 각도의 코사인 값을 이용하여 두 벡터의 유사한 정도 측정
- 유사도가 -1이면 서로 완전히 반대되는 경우
- 유사도가 0이면 서로 독립적인 경우
- 유사도가 1이면 서로 완전히 같은 경우
- 텍스트 매칭에 적용될 경우 두 벡터에 해당 문서에서의 단어 빈도가 적용

---

## 6. Embedding
- 한국어 임베딩 @ https://j.mp/3mduiBk