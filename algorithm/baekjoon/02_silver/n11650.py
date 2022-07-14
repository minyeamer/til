import sys

input = sys.stdin.readline
points = []

for _ in range(int(input())):
    points.append(tuple(map(int, input().split())))

for point in sorted(points):
    print(point[0], point[1])