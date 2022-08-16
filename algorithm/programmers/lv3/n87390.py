"""
0. Link
- https://school.programmers.co.kr/learn/courses/30/lessons/87390

1. Idea
- Greedy
- n의 크기가 굉장히 크기 때문에 2차원 배열을 만드는 것만으로 시간 초과가 발생할 것을 예상
- r행 c열의 값은 max(r,c)+1과 같고 1차원 배열의 인덱스 i에 대해 r은 i//n, c는 i%n와 동일
- left부터 right까지의 인덱스를 규칙에 맞는 값으로 변환하여 반환

2. Time Complexity
- O(N) = 10^5

3. Data Size
- n: 1 <= int <= 10^7
- left, right: 0 <= long <= n^2
- right - left < 10^5
"""

def solution(n, left, right):
    return [max(divmod(i,n))+1 for i in range(left,right+1)]