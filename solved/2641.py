n = int(input())
sample = [int(x) for x in input().split()]
k = int(input())
ans = []
for _ in range(k):
    orig = [int(x) for x in input().split()]
    rvsd = []
    for x in orig:
        if x == 1 or x == 2:
            rvsd.append(x+2)
        else:
            rvsd.append(x-2)
    rvsd.reverse()

    check = False
    for i in range(n):
        orig.append(orig.pop(0))
        if orig == sample:
            check = True
    for i in range(n):
        rvsd.append(rvsd.pop(0))
        if rvsd == sample:
            check = True
    if check:
        ans.append(' '.join([str(x) for x in orig]))
print(len(ans))
for a in ans:
    print(a)
