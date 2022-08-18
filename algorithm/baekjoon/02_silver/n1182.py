"""
0. Link
- https://www.acmicpc.net/problem/1182

1. Idea
- Brute Force
- 전체 배열에서 1부터 N개의 부분 조합을 완전탐색하면서 합이 S와 같은 경우를 카운트하고 출력

2. Data Size
- N: 1 <= int <= 20
- S: abs(int) <= 1,000,000
- arr: int(100,000) * N
"""

from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(1,N+1):
    comb = combinations(arr, i)
    count += sum(map(lambda x: sum(x)==S, comb))

print(count)