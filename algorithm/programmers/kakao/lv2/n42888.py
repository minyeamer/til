# Lv.2 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []

    record = [rec.split() for rec in record]
    name_dict = {rec[1]:rec[2] for rec in record if rec[0] in {'Enter','Change'}}
    msg_dict = {'Enter':'들어왔습니다.','Leave':'나갔습니다.'}

    for rec in record:
        if rec[0] in {'Enter','Leave'}:
            answer.append(name_dict[rec[1]]+'님이 '+msg_dict[rec[0]])

    return answer
