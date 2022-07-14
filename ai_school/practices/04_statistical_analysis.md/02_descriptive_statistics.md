# Descriptive Statistics
  1. [Chart](#1-chart)
     + [Pie Chart](#pie-chart)
     + [Bar Chart](#bar-chart)
  2. [Descriptive Statistics](#2-descriptive-statistics)
  3. [분포의 왜도와 첨도](#3-분포의-왜도와-첨도)
  4. [Outlier 탐지 및 제거](#4-outlier-탐지-및-제거)
     + [IQR 활용](#iqr-활용)
     + [Outlier 제거 전후 분포 비교](#outlier-제거-전후-분포-비교)
       + [Histogram](#histogram)
       + [Joint-Plot](#joint-plot)
  5. [Log 함수를 활용한 데이터 스케일링](#5-log-함수를-활용한-데이터-스케일링)

---

## 1. Chart

### Pie Chart

```python
df['column'].value_counts().plot(kind = 'pie')
```

![pie-chart](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FKxKGi%2Fbtryf1shG6C%2FFTgLpuK8AkNf0XRh46soU1%2Fimg.png)

### Bar Chart

```python
df['column'].value_counts().plot(kind = 'bar')
```

![bar-chart](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbrgC4k%2Fbtryc6VbSpu%2FU3cK7lWgor4WfPYCKcdGXk%2Fimg.png)

---

## 2. Descriptive Statistics
- `df['column'].max()`: 최댓값 (행방향 기준: `axis=1`)
- `df['column'].min()`: 최솟값
- `df['column'].sum()`: 합계
- `df['column'].mean()`: 평균
- `df['column'].variance()`: 분산
- `df['column'].std()`: 표준편차
- `df['column'].describe()`: 기술통계량

---

## 3. 분포의 왜도와 첨도
- `df['column'].hist()`: 히스토그램

![job-histogram](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdTuBCl%2FbtryhOlqZuZ%2FDdSxCudqahnwOhiugHzYF0%2Fimg.png)

- `df['column'].skew()`: 왜도 (분포가 좌우로 치우쳐진 정도)
- 왜도(Skewness): 0에 가까울수록 정규분포 (절대값 기준 3 미초과)   
  우측으로 치우치면 음(negative)의 왜도, 좌측으로 치우치면 양(positive)의 왜도
- `df['column'].kurtosis()`: 첨도 (분포가 뾰족한 정도)
- 첨도(Kurtosis): 1에 가까울수록 정규분포 (절대값 기준 8 또는 10 미초과)
- 왜도가 0, 정도가 1일 때 **완전한 정규분포**로 가정
- `sns.distplot(df['column'], rug=True)`: distribution plot   
  `rug`: 막대 그래프를 표시할지 여부

![sns-plot](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FXrdKR%2Fbtryeyxmtrl%2F43caX4DLVNgvqW6uHKSzt1%2Fimg.png)

- `sns.jointplot(x='column1', y='column2', data=df)`: 산점도와 히스토그램 한번에 표시

![joint-plot](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FYgaM5%2FbtryguHL5Uu%2FRjQz2usyrYV5CV3cUPZ020%2Fimg.png)

- `sns.jointplot(..., kind="kde")`: 밀집된 분포 곡선을 표시

![kde-plot](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbrYcq9%2FbtryhOy0Aa0%2FxkfyZuYRpBfM0wfFJbcsHK%2Fimg.png)

---

## 4. Outlier 탐지 및 제거
- `df.boxplot(column='column')`: 데이터 전체에 걸쳐서 분포 밀집도를 표시

![boxplot](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FqcwLb%2Fbtrye34Yp9z%2FW9XP5vXpkx25xhsUfD4Smk%2Fimg.png)

### IQR 활용
- IQR(Inter-Quantile Range): 바닥부터 75% 지점의 값 - 바닥부터 25% 지점의 값
- 상한치: 바닥부터 75% 지점의 값 + IQR의 1.5배
- 하한치: 바닥부터 25% 지점의 값 - IQR의 1.5배
- 상한/하한치를 넘으면 Outlier로 판단

```python
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)

IQR = Q3 - Q1

df_IQR = df[ (df['column'] < Q3 + IQR * 1.5) & (df['column'] > Q1 - IQR * 1.5) ]
df_IQR.boxplot(column='column')
```

![outlier-boxplot](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FIapzX%2Fbtryg3Da9ER%2FKF0FbmxIL4yM9KtmZDLamk%2Fimg.png)

### Outlier 제거 전후 분포 비교

#### Histogram

|Before|After|
|------|-----|
|![before](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcqDXT9%2Fbtryckfkqmp%2FULVs3Vd4bGaSQwAkzmk171%2Fimg.png)|![after](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fdm1qcl%2FbtryfiNQEz6%2FhdXXMFwbj7zrVPke4uku1K%2Fimg.png)|

#### Joint-Plot

|Before|After|
|------|-----|
|![jointplot-before](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlsTQQ%2FbtrydzQkllO%2FvakwmPQQMj5KcjdyGzywLK%2Fimg.png)|![jointplot-after](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlDL5y%2Fbtryg3b8jjO%2FE0buEf0mOEyYFDzdkJOrXk%2Fimg.png)|

---

## 5. Log 함수를 활용한 데이터 스케일링
- 왜도 혹은 첨도가 너무 큰 경우, Log 함수를 적용해 왜도/첨도를 낮춰주는 전처리를 적용
- `processed_df['log_column'] = np.log(processed_df['column'])`

|Before|After|
|------|-----|
|![log_before](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbDKDH1%2FbtrycC7SGvP%2FJdhxWeKAiz6FMlVl268IK0%2Fimg.png)|![log_after](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcC3nf5%2FbtryiGOgvp8%2Fsa2FOREjpWdkKYE8uOaV9k%2Fimg.png)|
