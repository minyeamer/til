"""
0. Link
- https://school.programmers.co.kr/learn/courses/30/lessons/43238

1. Idea
- Binary Search
- answer에 대한 이진탐색 수행 (1 <= answer <= max(times)*n)
- 매 탐색마다 answer 시간 동안 심사관들이 심사할 수 있는 사람의 수를 계산
- 심사한 사람의 수가 n명 이상일 경우 최대 범위를 조정하고 재탐색
- 심사한 사람의 수가 n명 미만일 경우 최소 범위를 조정하고 재탐색
- n명 이상의 사람을 심사할 수 있는 가장 작은 answer를 반환

2. Time Complexity
- Binary Search: O(M Log N^N) = 6,000,000

3. Data Size
- n: 1 <= int <= 1,000,000,000
- times: int(1,000,000,000) * 100,000
"""

def solution(n, times):
    answer = 0
    start, end = 1, max(times)*n

    while start <= end:
        mid = (start+end)//2
        passed = 0
        for time in times:
            passed += mid // time
            if passed >= n:
                break
        if passed >= n:
            answer = mid
            end = mid-1
        elif passed < n:
            start = mid+1

    return answer