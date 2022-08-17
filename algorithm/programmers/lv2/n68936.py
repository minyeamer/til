"""
0. Link
- https://school.programmers.co.kr/learn/courses/30/lessons/68936

1. Idea
- Divide and Conquer
- 2차원 배열을 4등분씩 나눠 재귀함수를 호출하고 동일한 값으로 채워져 있는지 판단하여 값의 개수 증가
- 2^n 형태의 정수에 대해 NumPy를 활용해 행렬 인덱싱을 간단히 구현

2. Time Complexity
- O(N^2 Log N^2) = 20,000,000

3. Data Size
- arr: [[int(1)]], shape(2^n, 2^n)
- 1 <= 2^n <= 1024
"""

import numpy as np

def quad_comp(n, arr, answer):
    values = np.unique(arr)
    if len(values) == 1:
        answer[values[0]] += 1
        return
    div = n//2
    quad_comp(div, arr[:div, :div], answer)
    quad_comp(div, arr[:div, div:], answer)
    quad_comp(div, arr[div:, :div], answer)
    quad_comp(div, arr[div:, div:], answer)

def solution(arr):
    arr = np.array(arr)
    answer = [0,0]
    quad_comp(len(arr), arr, answer)
    return answer