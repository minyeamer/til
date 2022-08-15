"""
0. Link
- https://www.acmicpc.net/problem/1463

1. Idea
- Dynamic Programming
- N에 대해 조건을 만족하는 경우에서 3으로 나누기, 2로 나누기, 1을 빼는 연산을 반복 수행하고   
  각각의 연산횟수 별로 도출할 수 있는 값을 모두 저장
- 앞선 결과를 모두 활용해 다음 결과에 대한 모든 경우를 탐색하고 결과 집합에 1이 있을 시 탐색을 종료
- 1이 포함된 마지막 집합의 인덱스 번호를 최소 연산횟수로 출력

2. Data Size
- N: 1 <= int <= 10^6
"""

N = int(input())
dp = [{N,}]
while 1 not in dp[-1]:
    dp.append(set())
    for n in dp[-2]:
        if n % 3 == 0:
            dp[-1].add(n//3)
        if n % 2 == 0:
            dp[-1].add(n//2)
        dp[-1].add(n-1)
print(len(dp)-1)