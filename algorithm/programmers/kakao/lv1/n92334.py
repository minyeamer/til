# Lv.1 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    report_dict = {id: 0 for id in id_list}
    mail_dict = {id: set() for id in id_list}

    for rep in set(report):
        user, target = rep.split()
        report_dict[target] += 1
        mail_dict[user].add(target)

    answer = []

    for user, targets in mail_dict.items():
        answer.append(sum([1 if report_dict[target] >= k else 0
                            for target in targets]))

    return answer
