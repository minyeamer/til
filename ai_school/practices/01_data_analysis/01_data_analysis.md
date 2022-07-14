# Data Analysis Practice
1. [Practice Data](#1-practice-data)
2. [범죄별로 검거율 계산](#2-범죄별로-검거율-계산)
    + [해당 계산법의 문제:](#해당-계산법의-문제)
    + [초과된 검거율을 최댓값으로 조정:](#초과된-검거율을-최댓값으로-조정)
    + [결측치를 의미있는 값으로 변경:](#결측치를-의미있는-값으로-변경)
3. [인구 데이터 Merge](#3-인구-데이터-merge)
    + [Pandas Merge Functions](#pandas-merge-functions)
4. [Additional Pandas Functions](#4-additional-pandas-functions)

---

## 1. Practice Data
- 서울시 범죄현황 통계자료

![original](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FEV1cR%2FbtrxcKjX1hr%2Fwv10EWTCQouzeNYL1ZaU4k%2Fimg.png)

---

## 2. 범죄별로 검거율 계산
```python
# gu_df는 실습 자료에 서울시 경찰청의 소속 구 데이터를 추가한 DataFrame
gu_df['강간검거율'] = gu_df['강간(검거)']/gu_df['강간(발생)']*100
gu_df['강도검거율'] = gu_df['강도(검거)']/gu_df['강도(발생)']*100
gu_df['살인검거율'] = gu_df['살인(검거)']/gu_df['살인(발생)']*100
gu_df['절도검거율'] = gu_df['절도(검거)']/gu_df['절도(발생)']*100
gu_df['폭력검거율'] = gu_df['폭력(검거)']/gu_df['폭력(발생)']*100
gu_df['검거율'] = gu_df['소계(검거)']/gu_df['소계(발생)']*100
```

![gu_df](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQ2V38%2Fbtrw5CadIj0%2FD4dPFOAxQh8PfNGcKZXVHk%2Fimg.png)

### 해당 계산법의 문제:
- 이전 연도에 발생한 사건이 많이 검거될 경우 검거율이 100%를 초과
- 발생 건수가 0인 경우 검거율에 결측치(N/A)가 발생

### 초과된 검거율을 최댓값으로 조정:
```python
# 검거율에 해당되는 열의 집합 columns
columns = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']
```
1. 모든 행에 대해 반복문 실행   
```python
for row_index, row in gu_df_rate.iterrows():
    for column in columns:
        if row[column] > 100:
            gu_df.at[row_index, column] = 100
```
2. Masking 기법 활용
```python
gu_df[ gu_df[columns] > 100 ] = 100
```
- `gu_df[columns] > 100`은 True와 False로 이루어진 행렬을 반환
- 해당 행렬을 `gu_df`의 Key로 사용하면 True에 해당하는 값이 채로 친듯 솎아 걸러짐
- 조건이 두 개 이상일 경우 괄호로 감싸주어야 함
- Pandas에서는 `and`, `or`, `not`이 동작하지 않기 때문에 `&`, `|`, `~` 사용
- `gu_df[ (gu_df['살인(발생)'] > 7) & (gu_df['폭력(발생)'] > 2000) ]`

### 결측치를 의미있는 값으로 변경:
```python
gu_df['살인검거율'] = gu_df['살인검거율'].fillna(100)
```

![adjusted_gu_df](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FoLSd4%2Fbtrxcx6elMY%2F9B1MmZeBKhqhF8FqfX5XD1%2Fimg.png)

---

## 3. 인구 데이터 Merge
```python
# 인구 데이터에 해당하는 csv 파일 불러오기
popul_df = pd.read_csv('pop_kor.csv', encoding='utf-8')
```

### Pandas Merge Functions
1. **Join:** `A.join(B)`
   - A와 B의 index 열이 동일해야 함
2. **Merge:** `pd.merge(A, B, left_on=, right_on=, how=)`
   - DataFrame A의 기준 `left_on`과 DataFrame B의 기준 `right_on`을 비교
   - `how` 옵션에는 inner (교집합), full_outer (합집합),   
     left_outer (A 기준 합), right_outer (B 기준 합) 가능
3. **Concatenate:** `pd.concat([A, B], axis=)`
   - 무조건 갖다 붙이기 때문에 사용에 주의

![merged_gu_df](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FI0FtH%2Fbtrw8PAiGP9%2F68TSIpom9MRT5OcXihlmKk%2Fimg.png)

---

## 4. Additional Pandas Functions
1. `df.iterrow()`: 반복문을 사용해 모든 행을 참조할 때 사용, (행 이름, Series) 반환
2. `df.at[]`: DataFrame에서 단일 값 추출 (단일 인덱싱에서 df.loc[]보다 빠름)
3. `df.[].fillna()`: 결측치(N/A)를 의미있는 값으로 바꿈 (Series가 가지고 있는 함수)
4. `df[df[]].str.contains()]`: 특정 문자가 포함된 행을 표시
5. Setting Index
   - `pd.read_csv('pop_kor.csv', encoding='utf-8', index_col=)`
   - `pd.read_csv('pop_kor.csv', encoding='utf-8').set_index()`
