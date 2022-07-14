# 소인수 분해

N = int(input())
count = 0
while N > 1:
    if N % 3 == 0:
        count += 1
        N //= 3
    elif N % 2 == 0:
        count += 1
        N //= 2
    else:
        count += 1
        N -= 1
print(count)