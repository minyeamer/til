"""
1. Idea
- Dynamic Programming
- P[i] = max(P[i-1]+V[i-1],P[i-1]-V[i-1]), 0 <= P[i] <= M
- 모든 P[i-1]가 P[i+1]에 영향을 줄 수 있기 때문에 범위 내 모든 값을 집합에 저장
- 마지막 곡에 대한 P가 존재할 경우 최댓값을 출력하고, 없을 경우 -1을 출력

2. Time Complexity
- DP: O(NM) = 50,000

3. Data Size
- N: 1 <= int <= 50
- M: 1 <= int <= 1,000
- S: 0 <= int <= M
- V: int * N
"""

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

P = [set() for _ in range(N+1)]
P[0] = {S,}

for i in range(1,N+1):
    for j in P[i-1]:
        if j+V[i-1] <= M:
            P[i].add(j+V[i-1])
        if j-V[i-1] >= 0:
            P[i].add(j-V[i-1])

if P[-1]:
    print(max(P[-1]))
else:
    print(-1)