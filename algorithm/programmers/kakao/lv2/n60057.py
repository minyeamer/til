# Lv.2 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)

    for unit in range(1,len(s)//2+1):
        s_range = list(range(0, len(s), unit))+[None]
        s_split = [s[s_range[i]:s_range[i+1]] for i in range(len(s_range)-1)]+['']
        new_s, memory, count = str(), s_split[0], 1
        for s_unit in s_split[1:]:
            if memory != s_unit:
                new_s += ((str(count) if count > 1 else str()) + memory)
                memory, count = s_unit, 1
            else:
                count += 1
        answer = min(answer, len(new_s))

    return answer
