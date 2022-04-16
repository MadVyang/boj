import sys


n, m = [int(x) for x in input().split()]
d = {}
for _ in range(n):
    site, pwd = sys.stdin.readline().strip().split()
    d[site] = pwd
for _ in range(m):
    print(d[sys.stdin.readline().strip()])
