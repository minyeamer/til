"""
0. Link
- https://www.acmicpc.net/problem/1676

1. Idea
- Math
- 팩토리얼 수를 구하고 문자열로 변환해 연속되는 0의 개수를 출력

2. Data Size
- N: 0 <= int <= 500
"""

from math import factorial
import re

N = int(input())
zeros = re.findall('0+', str(factorial(N)))
if zeros:
    print(len(zeros[-1]))
else:
    print(0)