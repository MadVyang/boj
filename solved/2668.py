n = int(input())
arr = []
for i in range(n):
    arr.append(int(input())-1)
v = [False]*n
check = [False]*n


def dfs(i, start):
    if v[i]:
        return False
    v[i] = True
    if i == start:
        check[i] = True
        return True
    if dfs(arr[i], start):
        check[i] = True
        return True
    return False


for i in range(n):
    v = [False]*n
    if arr[i] == i:
        check[i] = True
    elif dfs(arr[i], i):
        check[i] = True

# print(check)

count = 0
for i in range(n):
    if check[i]:
        count += 1
print(count)
for i in range(n):
    if check[i]:
        print(i+1)
