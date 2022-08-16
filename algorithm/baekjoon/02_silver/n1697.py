"""
0. Link
- https://www.acmicpc.net/problem/1697

1. Idea
- BFS
- N에서 시작해 K에 도달할 때까지 x-1, x+1, x*2에 대한 최단거리를 탐색
- 두 점이 위치할 수 있는 범위 내에서 가까운 거리의 점부터 탐색을 수행 K에 대한 거리를 출력
- N이 K보다 클 경우 x-1 외에는 이동수단이 없기 때문에 시간 단축을 위해 예외로 처리

2. Time Complexity
- O(N) = 100,000

3. Data Size
- N: 0 <= int <= 100,000
- K: 0 <= int <= 100,000
"""

from collections import deque

def bfs(start, target):
    MAX = 10**5
    count = [0] * (MAX+1)
    queue = deque([start])

    while queue:
        x = queue.popleft()
        if x == target:
            return count[x]
        for nx in (x-1,x+1,x*2):
            if 0 <= nx <= MAX and not count[nx]:
                count[nx] = count[x] + 1
                queue.append(nx)

N, K = map(int, input().split())

if N >= K:
    print(N - K)
else:
    print(bfs(N, K))