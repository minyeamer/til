N, M = map(int, input().split())
trees = list(map(int, input().split()))
mn, md, mx = 0, 0, max(trees)

while mn <= mx:
    md = (mx + mn) // 2
    total = 0
    for tree in trees:
        total += tree - md if tree > md else 0

    if total >= M:
        mn = md + 1
    else:
        mx = md - 1
print(mx)
