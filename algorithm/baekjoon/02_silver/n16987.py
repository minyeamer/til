"""
0. Link
- https://www.acmicpc.net/problem/16987

1. Idea
- Backtracking
- 0번째 계란부터 마지막 계란까지의 모든 경우의 수를 탐색
- 시간 단축을 위해 현재 계란이 깨진 경우 또는 나머지 모든 계란이 깨진 경우를 예외로 처리
- 한 번에 두 개 이상의 계란을 치는 경우를 방지하기 위해 계란을 친 후 원상복구 수행

2. Time Complexity
- Backtracking: O(N^N) = 16,777,216

3. Data Size
- N: 1 <= int <= 8
- S, W: 1 <= int <= 300
"""

N = int(input())
eggs = list()

for _ in range(N):
    eggs.append(list(map(int, input().split())))

answer = 0
def dfs(eggs, idx):
    global answer
    if idx == N:
        answer = max(answer, len([s for s,w in eggs if s < 1]))
        return

    if eggs[idx][0] < 1:
        dfs(eggs, idx+1)
        return

    if len([s for s,w in eggs if s < 1]) >= N-1:
        answer = max(answer, N-1)
        return

    for target in range(N):
        if target != idx and eggs[target][0] > 0:
            eggs[target][0] -= eggs[idx][1]
            eggs[idx][0] -= eggs[target][1]
            dfs(eggs, idx+1)
            eggs[target][0] += eggs[idx][1]
            eggs[idx][0] += eggs[target][1]

dfs(eggs, 0)
print(answer)