"""
0. Link
- https://www.acmicpc.net/problem/18870

1. Idea
- Sort
- 집합을 통해 압축한 unique한 좌표 목록을 정렬시키고,   
  정렬된 리스트 내에서 좌표와 인덱스를 딕셔너리로 맵핑

2. Time Complexity
- O(N Log N) = 13,000,000

3. Data Size
- N: 1 <= int <= 1,000,000
- X: -10^9 <= int <= 10^9
"""

N = int(input())
X = list(map(int, input().split()))
xtoi = {x:i for i,x in enumerate(sorted(set(X)))}
print(' '.join(map(lambda x: str(xtoi[x]), X)))