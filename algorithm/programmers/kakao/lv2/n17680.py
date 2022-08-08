"""
1. Idea
- LRU 알고리즘 (Deque로 구현)
- 도시이름이 캐시에 존재할 경우 시간에서 1 추가, 아닐 경우 5 추가
- 캐시에서 참고한 도시는 deque 최상단으로 재배치
- 캐시 사이즈를 초과할 경우 가장 오래된 도시를 제거

2. Time Complexity
- Deque: O(N) = 100,000

3. Data Size
- cacheSize: 0 <= int <= 30
- cities: str(20) * 100,000
"""

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            cache.append(city)
    return answer