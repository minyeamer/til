import math


N, M = map(int, input().split())
ladder, snake = dict(), dict()
board = [i for i in range(106)]

for _ in range(N):
    start, end = map(int, input().split())
    if end - start > 6:
        ladder[start] = end

for _ in range(M):
    start, end = map(int, input().split())
    snake[start] = end

# point, count = 1, 0
# while True:
#     next_points = board[point+1:point+7]
#     if 100 in next_points:
#         break
#     for next_point in next_points:
#         if next_point in snake.keys():
#             pass
#         if next_point in ladder.keys():

#     if True in [next_point in ladder.keys() for next_point in next_points]:
#         point = next_point


# print(sorted(ladder, key=lambda x: [math.ceil(x[0] - 1 / 6) + math.ceil(100 - x[1] / 6)]))



# 시작 위치는 1
# 1회 이동거리는 [1, 2, 3, 4, 5, 6]
# 사다리 정렬 > 단순 이동거리순
# 가장 높이 올라가는 사다리에 도달하도록
# 뱀을 타고 내려가서 다시 올라가는 것도
# 

# 고려사항
# 1. 가장 멀리 이동하는 사다리
# 1 -> 2 -> 76 (1)
# 76 -> 100 (6 * 4) = 5

# 2. 도착점과 가장 가까운 사다리
# 1 -> 31 -> 99 (6 * 5)
# 99 -> 100 (1) = 6

# 3. 최선
# 1 -> 2 -> 76 (1)
# 76 -> 77 -> 30 (1)
# 30 -> 31 -> 99 (1)
# 99 -> 100 (1) = 4

# v3
# 1. 사다리마다 단순 이동거리 구하기
# 2. 가장 이동거리가 짧은 사다리 우선 선택

# 2 -> 76
# 75 -> 30
# 31 -> 99

31

# 1. 가장 멀리가는 사다리로 이동하는 

# ladder
# 2 76
# 31 99
# 50 56
# 29 50

# snake
# 77 30
# 43 40
# 98 90
# 60 3