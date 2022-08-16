"""
0. Link
- https://www.acmicpc.net/problem/1541

1. Idea
- Greedy
- 최솟값을 만들기 위해서는 '-'를 기준으로 괄호를 치는 것이 최선
- '-'를 기준으로 식을 나누고 구분된 식을 계산하여 결과를 출력

2. Data Size
- arr: str(50)
"""

arr = input().split('-')
answer = sum(map(int,arr[0].split('+')))
for i in arr[1:]:
  answer -= sum(map(int,i.split('+')))
print(answer)