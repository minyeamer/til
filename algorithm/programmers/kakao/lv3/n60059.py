# Lv.3 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

import numpy as np
from itertools import product

def solution(key, lock):
    key, lock = np.array(key), np.array(lock)
    rotated_keys = [np.pad(np.rot90(key, i),len(lock)-1) for i in range(4)]

    index_list = list(range(len(rotated_keys[0])-len(lock)+1))
    for rotated_key in rotated_keys:
        for i, j in list(product(index_list, index_list)):
            key = rotated_key[i:i+len(lock),j:j+len(lock)]
            if (0 not in np.logical_or(key,lock)) and (2 not in (key + lock)):
                return True

    return False