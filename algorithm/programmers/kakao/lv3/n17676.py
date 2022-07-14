# Lv.3 [1차] 추석 트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676

from datetime import datetime, timedelta

def solution(lines):
    answer = 0
    lines = sorted(map(interpret_log, lines))

    delta = timedelta(seconds=1)
    for start in sum(lines, []):
        t = sum([check_time_range(time_range, start, start+delta) for time_range in lines])
        answer = max(t, answer)
        start += delta

    return answer

def interpret_log(line):
    line = line.split()
    line = [word.split(s) for word, s in zip(line, ['-',':','s'])]
    Y,m,d,H,M,S,ms = list(map(int,line[0]+line[1][:-1]+line[1][-1].split('.')))
    end_date = datetime(Y,m,d,H,M,S,ms*1000)
    duration = line[2][0] if '.' in line[2][0] else line[2][0]+'.0'
    S,ms = list(map(int,duration.split('.')))
    start_date = end_date - timedelta(seconds=S,milliseconds=ms-1)

    return [start_date, end_date]

def check_time_range(time_range, start, end):
    con1 = start <= time_range[0] < end
    con2 = time_range[0] <= start <= time_range[1]
    return con1 or con2
