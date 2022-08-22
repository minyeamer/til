"""
0. Link
- https://www.acmicpc.net/problem/1927

1. Idea
- Heapq
- 파이썬 heapq 모듈 자체가 최소힙이기 때문에 해당하는 기능을 활용하여 구현

2. Time Complexity
- O(Log N) = 16

3. Data Size
- N: 1 <= int <= 100,000
- x: 0 <= int < 2^31
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = list()

for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(arr, x)
    else:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)