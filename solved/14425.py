import sys


n, m = map(int, input().split())
s = set()
for i in range(n):
    s.add(sys.stdin.readline().strip())
ans = 0
for i in range(m):
    if sys.stdin.readline().strip() in s:
        ans += 1
print(ans)
