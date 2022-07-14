# Lv.3 표 편집
# https://programmers.co.kr/learn/courses/30/lessons/81303
# 풀이 중... 정확성은 전부 통과하는데 효율성이 꽝;;

import pandas as pd

def solution(n, k, cmd):
    """
    Case 1
    with pandas
    """

    cur = k
    # debug_dict = {0:'무지',1:'콘',2:'어피치',3:'제이지',4:'프로도',5:'네오',6:'튜브',7:'라이언'}
    table = pd.DataFrame([[i] for i in range(n)], columns=['data'])#.replace(debug_dict)
    memory = [table.copy()]
    move_cur = {'U':lambda mov,cur,mx: max(cur-mov, 0),
                'D':lambda mov,cur,mx: min(cur+mov, mx)}
    change_table = {'C':lambda cur,tab,mem: delete_table(cur,tab,mem),
                    'Z':lambda cur,tab,mem: restore_table(cur,tab,mem)}

    for c in cmd:
        if c[0] in {'U','D'}:
            cur = move_cur[c[0]](int(c.split()[1]), cur, len(table))
        else:
            cur, table, memory = change_table[c[0]](cur,table,memory)

    return ''.join(['O' if i in table['data'].tolist() else 'X' for i in range(n)])

def delete_table(cur, table, memory):
    table = table.drop(cur, axis=0)
    table['index'] = list(range(len(table)))
    table = table.set_index('index')
    cur = cur-1 if cur > len(table)-1 else cur
    memory.append(table.copy())
    return cur, table, memory

def restore_table(cur, table, memory):
    cur_data = table.loc[cur][0]
    memory.pop()
    table = memory[-1].copy()
    cur = table[table['data'] == cur_data].index[0]
    return cur, table, memory


def solution(n, k, cmd):
    """
    Case 2
    with set
    """

    table = {i for i in range(n)}
    memory = list()
    cur, min_cur, max_cur = k, 0, n-1

    for c in cmd:
        if c[0] in {'U','D'}:
            cur = move_cur(c[0],cur,int(c.split()[1]),table,min_cur,max_cur)
        elif c[0] == 'C':
            memory.append(cur)
            table.discard(cur)
            if min_cur == cur:
                min_cur = cursor_down(min_cur,1,table,max_cur)
                cur = min_cur
            elif max_cur == cur:
                max_cur = cursor_up(max_cur,1,table,min_cur)
                cur = max_cur
            else:
                cur = cursor_down(cur,1,table,max_cur)
        elif c[0] == 'Z':
            hist = memory.pop()
            table.add(hist)
            min_cur = hist if hist < min_cur else min_cur
            max_cur = hist if hist > max_cur else max_cur

    return ''.join(['O' if i in table else 'X' for i in range(n)])

def move_cur(cmd, cur, mov, table, min_cur, max_cur):
    if cmd == 'U':
        return cursor_up(cur, mov, table, min_cur)
    elif cmd == 'D':
        return cursor_down(cur, mov, table, max_cur)

def cursor_up(cur, mov, table, min_cur):
    for _ in range(mov):
        if cur == min_cur:
            return cur
        cur -= 1
        while cur not in table:
            cur -= 1
    return cur

def cursor_down(cur, mov, table, max_cur):
    for _ in range(mov):
        if cur == max_cur:
            return cur
        cur += 1
        while cur not in table:
            cur += 1
    return cur
