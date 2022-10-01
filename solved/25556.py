from collections import deque


n = int(input())
arr = [int(x) for x in input().split()]

st = [deque(), deque(), deque(), deque()]

for i in arr:
    mn = 123456
    sj = -1
    for j in range(4):
        if st[j] and st[j][-1] < i and i-st[j][-1] < mn:
            sj = j
            mn = i-st[j][-1]
        elif not st[j] and i<mn:
            sj = j
            mn = i
    if sj == -1:
        break
    st[sj].append(i)

sm = 0
for s in st:
    sm += len(s)
if sm == n:
    print('YES')
else:
    print('NO')
