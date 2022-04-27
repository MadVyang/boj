n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr.sort()
mark = set()
sel = []


def dfs(i, count):
    global n, m
    if count == m:
        s = ' '.join([str(x) for x in sel])
        if s in mark:
            return
        mark.add(s)
        print(s)
        return
    for j in range(i, n):
        sel.append(arr[j])
        dfs(j, count+1)
        sel.pop()


dfs(0, 0)
