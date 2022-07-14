# Lv.1 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub(r"[^a-z0-9-_\.]","",answer)
    answer = re.sub(r"\.+",".",answer)
    answer = re.sub(r"^\.","",answer)
    answer = re.sub(r"\.$","",answer)
    answer = 'a' if not answer else answer
    answer = answer[:15]
    answer = answer[:-1] if answer[-1] == '.' else answer
    answer += answer[-1]*(3-len(answer))
    return answer
