import math
import sys


n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().strip().split()])


def solve():
    mn = math.inf
    for i in range(n-1):
        a, b = arr[i]
        c, d = arr[i+1]
        mn = min(mn, (a-c)*(a-c)+(b-d)*(b-d))
    return mn


arr.sort(key=lambda x: x[0])
ans = solve()
arr.sort(key=lambda x: x[1])
ans = min(ans, solve())
print(ans)
