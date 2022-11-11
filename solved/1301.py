n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
num = sum(arr)
remains = arr[:]


def remains_to_number():
    r = 0
    for i in range(n):
        r *= 11
        r += remains[i]
    return r


mem = {}


def dfs(count, b1, b2):
    rn = remains_to_number()
    if (rn, b1, b2) in mem:
        return mem[(rn, b1, b2)]
    global num
    if count == num:
        return 1
    r = 0
    for i in range(n):
        if i not in [b1, b2] and remains[i] > 0:
            remains[i] -= 1
            r += dfs(count+1, b2, i)
            remains[i] += 1
    mem[(rn, b1, b2)] = r
    return r


print(dfs(0, -1, -1))
