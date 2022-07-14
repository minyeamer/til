# Processing Text Data
  1. [NLTK Library](#1-nltk-library)
  2. [문장을 단어 수준에서 토큰화](#2-문장을-단어-수준에서-토큰화)
  3. [POS Tagging](#3-pos-tagging)
     + [NLTK POS Tags List](#nltk-pos-tags-list)
  4. [Stopwords 제거](#4-stopwords-제거)
  5. [Lemmatizing](#5-lemmatizing)
     + [영화 리뷰 데이터 전처리](#영화-리뷰-데이터-전처리)

---

## 1. NLTK Library
- NLTK(Natural Language Toolkit)은 자연어 처리를 위한 라이브러리
```python
import nltk

nltk.download()
```

---

## 2. 문장을 단어 수준에서 토큰화
```python
sentence = 'NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.'

nltk.word_tokenize(sentence)
```

#### Output
```vim
['NLTK',
 'is',
 'a',
 'leading',
 'platform',
 ...
```

---

## 3. POS Tagging

```python
tokens = nltk.word_tokenize(sentence)
nltk.pos_tag(tokens)
```

#### Output
```vim
[('NLTK', 'NNP'),
 ('is', 'VBZ'),
 ('a', 'DT'),
 ('leading', 'VBG'),
 ('platform', 'NN'),
 ...
```

### NLTK POS Tags List

![nltk_pos_tags_1](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb8AI88%2FbtrxjH12WYy%2Fi9DoCLPtIU4YrE07pt39Lk%2Fimg.png)

![nltk_pos_tags_2](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbEbtoD%2Fbtrxiaql38x%2FTz60KM1pMrm7ddzj6KwCt1%2Fimg.png)

---

## 4. Stopwords 제거
```python
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
stop_words.append(',')
stop_words.append('.')

result = []

for token in tokens:
    if token.lower() not in stopWords:
        result.append(token)
```

#### Output
```python
['NLTK', 'leading', 'platform', 'building', 'Python', 'programs', 'work', 'human', 'language', 'data', 'provides', 'easy-to-use', 'interfaces', '50', 'corpora', 'lexical', 'resources', 'WordNet', 'along', 'suite', 'text', 'processing', 'libraries', 'classification', 'tokenization', 'stemming', 'tagging', 'parsing', 'semantic', 'reasoning', 'wrappers', 'industrial-strength', 'NLP', 'libraries', 'active', 'discussion', 'forum']
```

---

## 5. Lemmatizing
- **Lemmatization:** 단어의 형태소적/사전적 분석을 통해 파생적 의미를 제거하고,   
어근에 기반하여 기본 사전형인 **lemma**를 찾는 것

```python
lemmatizer = nltk.wordnet.WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))             # cat
print(lemmatizer.lemmatize("geese"))            # goose

print(lemmatizer.lemmatize("better"))           # better
print(lemmatizer.lemmatize("better", pos="a"))  # good

print(lemmatizer.lemmatize("ran"))              # ran
print(lemmatizer.lemmatize("ran", 'v'))         # run
```

- default로 `n` 이므로 'cats', 'geese' 들은 기본명사형을 반환
- 형용사 'better'는 `pos`에 `a`를 함께 입력해주어야 원형인 'good'을 반환
- 동사 'ran'은 `pos`에 `v`를 함께 입력해주어야 원형인 'run'을 반환

### 영화 리뷰 데이터 전처리
```python
file = open('moviereview.txt', 'r', encoding='utf-8')
lines = file.readlines()

sentence = lines[1]
tokens = nltk.word_tokenize(sentence)

lemmas = []
for token in tokens:
    if token.lower() not in stop_words:
        lemmas.append(lemmatizer.lemmatize(token))
```