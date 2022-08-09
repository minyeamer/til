"""
1. Idea
- LZW 알고리즘 (List로 구현)
- 단어를 문자 단위로 탐색하면서 캐시에 추가
- 캐시가 문자 사전에 없을 경우 이전 문자까지의 인덱스를 반환하고,   
  캐시를 문자 사전에 추가

2. Time Complexity
- Brute-Force: O(N^2) = 1000000

3. Data Size
- msg: str(1000)
"""

def solution(msg):
    answer = []
    chars = [chr(x) for x in range(64,91)]

    cache = str()
    for c in msg:
        cache += c
        if cache not in chars:
            answer.append(chars.index(cache[:-1]))
            chars.append(cache)
            cache = c
    answer.append(chars.index(cache))

    return answer