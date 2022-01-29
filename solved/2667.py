n = int(input())
arr = []
for _ in range(n):
    arr.append([x for x in input()])


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(i, j, c):
    if i < 0 or j < 0 or i == n or j == n:
        return False
    if arr[i][j] == '1':
        arr[i][j] = c
        for d in dirs:
            dfs(i+d[0], j+d[1], c)
        return True


count = 2
for i in range(n):
    for j in range(n):
        if dfs(i, j, count):
            count += 1
counts = [0]*count
for i in range(n):
    for j in range(n):
        if arr[i][j] == '0':
            continue
        counts[arr[i][j]] += 1

print(count-2)
counts.sort()
for i in range(2, count):
    print(counts[i])
