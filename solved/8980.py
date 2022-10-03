import sys


n, c = [int(x) for x in input().split()]
m = int(input())
arr = []
for i in range(m):
    a, b, cc = [int(x) for x in sys.stdin.readline().strip().split()]
    arr.append((a, b, cc))
arr.sort(key=lambda x: (x[1]))

ans = 0
carry = [0]*(n+1)
for i, j, k in arr:
    mx = max(carry[i:j])
    if mx+k <= c:
        add = k
    else:
        add = c-mx
    for idx in range(i, j):
        carry[idx] += add
    ans += add
print(ans)
