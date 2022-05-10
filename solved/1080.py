import sys


n, m = [int(x) for x in sys.stdin.readline().strip().split()]
A = [[int(x) for x in sys.stdin.readline().strip()] for i in range(n)]
B = [[int(x) for x in sys.stdin.readline().strip()] for i in range(n)]


def p(i, j):
    for y in range(3):
        for x in range(3):
            A[i+y][j+x] = 1-A[i+y][j+x]


count = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            count += 1
            p(i, j)

for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            count = -1
            break
print(count)
