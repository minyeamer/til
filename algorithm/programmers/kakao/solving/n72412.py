# Lv.3 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412
# 풀이 중... pandas는 느려...

import pandas as pd

def solution(info, query):
    answer = list()
    columns = ['언어','직군','경력','소울 푸드','점수']
    table = pd.DataFrame([i.split() for i in info],columns=columns)
    table['점수'] = table['점수'].astype(int)
    queries = [q.split() for q in query]

    for query in queries:
        query_tabe = table.copy()
        score, query = int(query[-1]), [query[i].replace('-','') for i in range(len(query)-1) if i%2==0]
        for col, que, in zip(columns, query):
            query_tabe = query_tabe[query_tabe[col].str.contains(que)]
        answer.append(sum(query_tabe['점수'] >= score))

    return answer