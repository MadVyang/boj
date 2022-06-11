n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append([int(x) for x in input().split()])

for i in range(n):
    t = [int(x) for x in input().split()]
    for j in range(m):
        arr[i][j] += t[j]
for i in range(n):
    print(' '.join([str(x) for x in arr[i]]))
