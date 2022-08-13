"""
0. Link
- https://school.programmers.co.kr/learn/courses/30/lessons/42895

1. Idea
- Dynamic Programming
- S[1] = {N}
- S[2] = {NN, N+N, N-N, N*N, N/N}
- S[3] = {NNN, S[2][x] (+,-,*,/) S[1][y], ...}
- 2부터 8까지의 범위를 가진 i와 1부터 i-1까지의 범위를 가진 j에 대해,   
  S[j]와 S[i-j]의 사칙연산 결과를 S[i]에 추가하고 해당 집합이 number를 포함하는지 검증

2. Time Complexity
- DP: O(1)

3. Data Size
- N: 1 <= int <= 9
- number: 1 <= int <= 32,000
- answer: int <= 8
"""

from itertools import product

def solution(N, number):
    S = [set() for _ in range(9)]

    if N == number:
        return 1
    else:
        S[1].add(N)

    for i in range(2,9):
        S[i].add(int(str(N)*i))
        for j in range(1,i):
            for x,y in product(S[j],S[i-j]):
                S[i].update({x+y,x-y,x*y})
                if y != 0:
                    S[i].add(x//y)
        if number in S[i]:
            return i
    return -1