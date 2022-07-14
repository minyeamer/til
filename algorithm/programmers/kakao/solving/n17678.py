# Lv.3 [1차] 셔틀버스
# https://programmers.co.kr/learn/courses/30/lessons/17678
# 풀이 중... 생각해야 할 조건이 너무 많음;;

from datetime import datetime, timedelta
from collections import Counter

def solution(n, t, m, timetable):
    date_time = lambda t: datetime(1,1,1,t[0],t[1])
    sum_cnt = lambda t: sum([cnt for crew,cnt in t])

    bustable = [date_time((0,0))]+[date_time((9,0))+timedelta(minutes=t*i) for i in range(n)]
    timetable = Counter([date_time(tuple(map(int,t.split(':')))) for t in timetable ])
    timetable = sorted([(crew,cnt) for crew,cnt in timetable.items() if crew<=bustable[-1]],reverse=True)

    if not timetable:
        return bustable[-1].strftime('%H:%M')

    for i in range(1,len(bustable)):
        if bustable[i] < timetable[-1][0]:
            continue
        onboard = list()
        while sum_cnt(onboard) < m:
            onboard.append(timetable.pop())
            if (not timetable) or (bustable[i] < timetable[-1][0]):
                break
            if sum_cnt(onboard) > m:
                timetable.append((onboard[-1][0],(sum_cnt(onboard)-m)))
        if sum_cnt(onboard) < m:
            if not timetable:
                return bustable[-1].strftime('%H:%M')
        else:
            if (sum_cnt(timetable)+sum_cnt(onboard)) >= m*(n-i+1):
                return (onboard[-1][0]-timedelta(minutes=1)).strftime('%H:%M')
