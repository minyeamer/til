"""
0. Link
- https://www.acmicpc.net/problem/2302

1. Idea
- Dynamic Programming
- 자리를 옮길 수 있는 연속되는 좌석의 수는 피보나치 수열을 따름 (S[i] = F[i+1])
- VIP 좌석 번호를 기준으로 연속되는 좌석의 수를 리스트로 저장
- 모든 연속되는 좌석 수에 대한 피보나치 수를 곱하고 출력

1-1. Sequence
S2 (1,2) -> (1,2), (2,1) = 2(F3)
S3 (1,2,3) -> (1,2,3), (2,1,3), (1,3,2) = 3(F4)
S4 (1,2,3,4) -> (1,2,3,4), (2,1,3,4), (1,2,4,3), (1,3,2,4), (2,1,4,3) = 5(F5)
S5 (1,2,3,4,5) -> (1,2,3,4,5), (1,2,4,3,5), (1,2,3,5,4), (2,1,3,4,5), (2,1,4,3,5), (2,1,3,5,4), (1,3,2,4,5), (1,3,2,5,4) = 8(F6)
S6 (1,2,3,4,5,6) -> (1,2,3,4,5,6), (1,2,4,3,5,6), (1,2,3,5,4,6), (1,2,3,4,6,5), (1,2,4,3,6,5), ...

2. Time Complexity
- DP: O(N) = 40

3. Data Size
- N: 1 <= int <= 40
- M: 0 <= int <= N
- answer: int < 2^31-1
"""

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

seats, idx = list(), 0
for _ in range(M):
    vip = int(input())
    seats.append(vip-idx-1)
    idx = vip
seats.append(N-idx)

F = {1:1, 2:1}
def fibonacci(n):
    if n in F:
        return F[n]
    F[n] = fibonacci(n-1) + fibonacci(n-2)
    return F[n]

answer = 1
for seat in seats:
    if seat > 1:
        answer *= fibonacci(seat+1)

print(answer)