arr = []
for i in range(9):
    arr.append(int(input()))

sel = []
sum = 0


def solve(i):
    global sum
    if len(sel) == 7 and sum == 100:
        show()
        return
    if i == 9:
        return
    sel.append(arr[i])
    sum += arr[i]
    solve(i+1)
    sel.pop()
    sum -= arr[i]
    solve(i+1)


def show():
    for i in sel:
        print(i)


solve(0)
