"""
0. Link
- https://www.acmicpc.net/problem/21318

1. Idea
- Prefix Sum
- 실수한 곡에 대한 누적합을 구하고 인덱싱을 통해 특정 구간에 대한 누적합 출력
- 마지막 곡은 항상 성공하기 때문에 y에 대한 누적합과 y-1에 대한 누적합이 다르면 1 감소

2. Time Complexity
- Prefix Sum: O(N) = 100,000

3. Data Size
- N: 1 <= int <= 100,000
- scores: int(10^9) * N
- Q: 1 <= int <= 100,000
"""

import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
Q = int(input())

fails = [0]*(N+1)
for i in range(1,N+1):
    fails[i] = fails[i-1] + int(scores[i-1] > scores[min(i,N-1)])

for _ in range(Q):
    x, y = map(int, input().split())
    answer = fails[y] - fails[x-1]
    if fails[y] != fails[y-1]:
        answer -= 1
    print(answer)