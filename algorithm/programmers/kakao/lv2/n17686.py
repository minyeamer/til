"""
1. Idea
- 정규표현식을 활용해 HEAD, NUMBER, TAIL을 분리
- 전체 파일명을 완전탐색하면서 리스트에 분리된 파일명을 저장
- HEAD와 NUMBER를 기준으로 파일명을 정렬하고 정렬된 원본 파일명을 반환

2. Time Complexity
- Brute-Force + Sort: O(NM+NlogN)) = 110000

3. Data Size
- files: str(100) * 1000
"""

import re

def solution(files):
    answer = []

    for file in files:
        head, number, tail = re.findall('([^0-9]+)([0-9]+)(.*)', file)[0]
        answer.append((head.lower(), int(number), tail, file))
    answer.sort(key=lambda x: [x[0],x[1]])

    return [file for _,_,_,file in answer]