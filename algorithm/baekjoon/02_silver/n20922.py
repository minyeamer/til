"""
0. Link
- https://www.acmicpc.net/problem/20922

1. Idea
- Two Pointer
- 수열의 시작과 끝 지점에 대한 두 개의 포인터 지정
- 끝 지점에 대한 포인터를 확장하면서 탐색되는 원소의 수를 카운트
- 원소의 수가 K개와 같아지는 시점부터 시작 지점에 대한 포인터를 확장하여 범위 축소
- 최종적으로 두 포인터 간 거리의 최대치를 출력

2. Time Complexity
- O(N) = 200,000

3. Data Size
- N: 1 <= int <= 200,000
- K: 1 <= int <= 100
- a: int(100,000) * N
"""

N, K = map(int, input().split())
a = list(map(int, input().split()))
answer = 0
start, end = 0, 0
counter = [0] * (max(a)+1)

while end < N:
    if counter[a[end]] < K:
        counter[a[end]] += 1
        end += 1
    else:
        counter[a[start]] -= 1
        start += 1
    answer = max(end-start, answer)

print(answer)