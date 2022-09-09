import math


x, y, d, t = map(int, input().split())


def eq(a, b):
    return abs(a-b) < 1e-10


dist = math.sqrt(x*x+y*y)
n = int(dist/d)
cur = dist
if n > 0:
    cur = min(cur, t*n+dist-d*n)
    cur = min(cur, t*(n+1))
    cur = min(cur, t*(n+1)+d*(n+1)-dist)
else:
    cur = min(cur, t+d-dist)
    cur = min(cur, t*2)
# print(n)
print(cur)