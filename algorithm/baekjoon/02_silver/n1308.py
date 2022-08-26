"""
0. Link
- https://www.acmicpc.net/problem/1308

1. Idea
- 각각의 날짜에 대한 문자열을 date 타입으로 변환하고, today 기준 1000년 후 날짜와 dday를 비교
- 조건이 맞을 경우 'gg'를 출력하고, 아니면 두 날짜의 차이를 출력

2. Data Size
- y,m,d: 1,1,1 <= int*3 <= 9999,12,31
"""

from datetime import date
strptime = lambda: date(**{k:int(v) for k,v in zip(['year','month','day'],input().split())})
today, dday = strptime(), strptime()
if dday >= today.replace(today.year+1000):
    print('gg')
else:
    print('D-'+str((dday-today).days))