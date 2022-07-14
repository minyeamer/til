# Text Data Exploration
  1. [Tokenizing Text Data](#1-tokenizing-text-data)
     + [Import Libraries](#import-libraries)
     + [Set Stopwords](#set-stopwords)
     + [Open Text Data](#open-text-data)
     + [Tokenize](#tokenize)
  2. [Counting Nouns](#2-counting-nouns)
     + [POS Tagging](#pos-tagging)
     + [Counting Nouns](#counting-nouns)
  3. [Counting Adjectives](#3-counting-adjectives)
     + [POS Tagging](#pos-tagging-1)
     + [Counting Adjectives](#counting-adjectives)
  4. [Counting Verbs](#4-counting-verbs)
     + [POS Tagging](#pos-tagging-2)
     + [Counting Verbs](#counting-verbs)
  5. [Visualizing Tokens](#5-visualizing-tokens)
     + [Import Libraries](#import-libraries-1)
     + [정규표현식으로 토큰 분류](#정규표현식으로-토큰-분류)
     + [Visualizing Tokens](#visualizing-tokens)
     + [Top 25 Words Chart](#top-25-words-chart)
  6. [Similar Words](#6-similar-words)
  7. [Collocation](#7-collocation)

---

## 1. Tokenizing Text Data

### Import Libraries
```python
import nltk
from nltk.corpus import stopwords
from collections import Counter
```

### Set Stopwords
```python
stop_words = stopwords.words("english")
stop_words.append(',')
stop_words.append('.')
stop_words.append('’')
stop_words.append('”')
stop_words.append('—')
```

### Open Text Data
```python
file = open('movie_review.txt', 'r', encoding="utf-8")
lines = file.readlines()
```

### Tokenize
```python
tokens = []
for line in lines:
    tokenized = nltk.word_tokenize(line)
    for token in tokenized:
        if token.lower() not in stop_words:
            tokens.append(token)
```

---

## 2. Counting Nouns

### POS Tagging
```python
tags = nltk.pos_tag(tokens)

word_list = []
for word, tag in tags:
    if tag.startswith('N'):
        word_list.append(word.lower())
```

### Counting Nouns
```python
counts = Counter(word_list)
print(counts.most_common(10))
```

### Output
```python
[('movie', 406), ('batman', 303), ('film', 284), ('joker', 219), ('dark', 136), ('ledger', 131), ('knight', 124), ('time', 112), ('heath', 110), ('performance', 87)]
```

---

## 3. Counting Adjectives

### POS Tagging
```python
tags = nltk.pos_tag(tokens)

word_list = []
for word, tag in tags:
    if tag.startswith('J'):
        word_list.append(word.lower())
```

### Counting Adjectives
```python
counts = Counter(word_list)
print(counts.most_common(10))
```

### Output
```python
[('good', 141), ('best', 102), ('great', 78), ('many', 54), ('much', 52), ('comic', 43), ('real', 29), ('bad', 28), ('little', 26), ('new', 25)]
```

---

## 4. Counting Verbs

### POS Tagging
```python
tags = nltk.pos_tag(tokens)

word_list = []
for word, tag in tags:
    if tag.startswith('V'):
        word_list.append(word.lower())
```

### Counting Verbs
```python
counts = Counter(word_list)
print(counts.most_common(10))
```

### Output
```python
[('see', 59), ('get', 54), ('made', 49), ('think', 46), ('seen', 45), ('make', 45), ('say', 41), ("'ve", 37), ("'m", 32), ('going', 31)]
```

---

## 5. Visualizing Tokens

### Import Libraries
```python
import matplotlib.pyplot as plt
import re
```

### 정규표현식으로 토큰 분류
```python
tokens = []

for line in lines:
    tokenized = nltk.word_tokenize(line)
    for token in tokenized:
        if token.lower() not in stop_words:
            if re.match('^[a-zA-Z]+', token):
                tokens.append(token)
```
- 정규표현식 개념 소개 @ https://j.mp/3bJQJHg
- 정규표현식 기본 문법 정리 @ https://j.mp/3bLXSqB
- 상세한 정규표현식 설명 @ http://j.mp/2PzgFO8
- 상세한 정규표현식 예제 @ https://hamait.tistory.com/342
- 점프 투 파이썬 정규표현식 @ https://wikidocs.net/4308

### Visualizing Tokens
```python
plt.figure(figsize=(10, 3)) 
plt.title('Top 25 Words',fontsize=30)

corpus.plot(25)
```

### Top 25 Words Chart

![token_chart](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FrwAVx%2FbtrxgGi3cGZ%2FmC4YxRl6LRgwRG63YMIjCk%2Fimg.png)

---

## 6. Similar Words
```python
print('Similar words : ')
corpus.similar('batman')
```

#### Output
```vim
Similar words : 
superhero film action movie character better iconic seen acting actor heath performance modern difficult villain second end good come best
```

---

## 7. Collocation
```python
print('Collocation')
corpus.collocation())
```

#### Output
```vim
Collocation
Dark Knight; Heath Ledger; Christian Bale; comic book; Harvey Dent; Christopher Nolan; Bruce Wayne; Aaron Eckhart; Morgan Freeman; Gary Oldman; Batman Begins; Two Face; Gotham City; Maggie Gyllenhaal; Rachel Dawes; Michael Caine; special effect; Tim Burton; Jack Nicholson; dark knight
```