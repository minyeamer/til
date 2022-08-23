"""
0. Link
- https://www.acmicpc.net/problem/1931

1. Idea
- Sliding Window
- 슬라이딩 윈도우의 전형적인 문제로, 끝 시간을 기준으로 시간을 정렬해서 겹치지 않는 수를 계산

2. Time Complexity
- O(N) = 100,000

3. Data Size
- N: 1 <= int <= 100,000
- t1,t2: 0 <= int <= 2^31-1
"""

import sys
input = sys.stdin.readline

N = int(input())
times = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: [x[1],x[0]])
count, end_time = 0, 0

for t1,t2 in times:
    if t1 >= end_time:
        count += 1
        end_time = t2

print(count)