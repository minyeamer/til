"""
0. Link
- https://school.programmers.co.kr/learn/courses/30/lessons/17687

1. Idea
- Math
- 0부터 시작해 t*m의 길이를 만족하는 N진법 배열을 생성
- 매 순서마다 p 위치에 해당하는 값을 추출해 문자열로 반환

2. Data Size
- n: 2 <= int <= 16
- t: 0 < int <= 1,000
- m: 2 <= int <= 100
- p: 1 <= int <= m
"""

alpha = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def n_base(num, base):
    result = str()
    while num > 0:
        num, mod = divmod(num, base)
        result += str(mod) if mod < 10 else alpha[mod]
    return result[::-1]

def solution(n, t, m, p):
    arr = '01'
    total = t*m
    p = p%m

    i = 2
    while len(arr) < total:
        arr += n_base(i, n)
        i += 1

    answer = [t for i,t in enumerate(arr[:total]) if (i+1)%m==p]
    return ''.join(answer)