n = int(input())
arr = []
i = 1
while i*i <= n:
    arr.append(i*i)
    i += 1


def solve(current, current_i, count, max_count):
    if count == max_count:
        return current == 0
    if current <= 0:
        return False
    r = False
    for i in range(current_i, len(arr)):
        r = r or solve(current-arr[i], i, count+1, max_count)
    return r


for i in range(1, 5):
    if solve(n, 0, 0, i):
        print(i)
        break
