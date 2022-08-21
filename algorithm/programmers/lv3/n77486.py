"""
0. Link
- https://school.programmers.co.kr/learn/courses/30/lessons/77486

1. Idea
- Union-Find 알고리즘의 Find() 함수를 사용하여 부모 노드에 대해 재귀적으로 접근
- 최악의 경우 O(NM)=10^10으로 시간 초과가 발생하지만,
  매 탐색마다 최대 10,000원을 10씩 나눠 0이 되는 순간에 재귀가 종료되기 때문에 최대 깊이가 5로 좁혀짐

2. Time Complexity
- O(N) = 100,000

3. Data Size
- enroll, referral: str(10) * 10,000
- seller: str(10) * 100,000
- amount: int(100) * 100,000
"""

def find(parents, cur, income, answer):
    alloc = income//10
    if parents[cur] == cur or alloc == 0:
        answer[cur] += income-alloc
        return
    answer[cur] += income-alloc
    find(parents, parents[cur], alloc, answer)
    return

def solution(enroll, referral, seller, amount):
    N = len(enroll)
    answer = [0] * N
    name2id = {name:i for i,name in enumerate(enroll)}
    parents = [i if referral[i]=='-' else name2id[referral[i]] for i in range(N)]
    for i in range(len(seller)):
        find(parents, name2id[seller[i]], amount[i]*100, answer)
    return answer