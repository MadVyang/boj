import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = []
for i in range(n):
    arr.append([True]*n)
for i in range(m):
    a, b = map(int, input().strip().split())
    arr[a-1][b-1] = False
    arr[b-1][a-1] = False

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i][j] and arr[i][k] and arr[j][k]:
                ans += 1
print(ans)
