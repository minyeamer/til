"""
1. Idea
- 악보 정보에서 #이 포함된 음을 소문자로 대체하고 완전탐색
- 시간 계산은 timedelta 활용
- (재생시간,제목)으로 구성된 리스트를 정렬

2. Time Complexity
- Brute-Force: O(NM) = 143,900

3. Data Size
- m: 1 <= int <= 1439
- musicinfos: list <= 100
- musicinfos[0,1]: HH:MM (00:00 - 23:59)
- musicinfos[2]: str(64)
- musicinfos[4]: 1 <= int <= 1439
"""

import datetime as dt
import re
import math

def solution(m, musicinfos):
    answer = list()

    lower_repl = lambda match: match.group(1)[0].lower()
    sharp_repl = lambda s: re.sub('([A-G]#)', lower_repl, s)
    m = sharp_repl(m)
    strptime = lambda x: dt.timedelta(hours=int(x[0]),minutes=int(x[1]))

    for info in musicinfos:
        start, end, title, chord = info.split(',')
        plays = (strptime(end.split(':'))-strptime(start.split(':'))).seconds//60
        chord = sharp_repl(chord)
        chord = (chord * math.ceil(plays/len(chord)))[:plays]
        if m in chord:
            answer.append((plays,title))

    return sorted(answer, key=lambda x: x[0], reverse=True)[0][1] if len(answer) else '(None)'