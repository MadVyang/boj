import sys
sys.setrecursionlimit(100030)

t = int(input())
arr = []
check = []
trash = []
v = []

count = 0


def solve(current, call_count):
    global count
    if trash[current]:
        return False
    if check[current]:
        trash[current] = True
        return False
    if v[current] > 0:
        count += call_count-v[current]
        check[current] = True
        return True
    v[current] = call_count
    if solve(arr[current], call_count+1):
        check[current] = True
    else:
        trash[current] = True


for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [int(x)-1 for x in sys.stdin.readline().split()]
    is_solo = [arr[x] == x for x in range(n)]
    check = [arr[x] == x for x in range(n)]
    trash = [False for x in range(n)]
    v = [0]*n

    count = 0
    for i in range(n):
        if is_solo[i]:
            count += 1
        elif not trash[i] and not check[i]:
            if solve(i, 1):
                check[i] = True
            else:
                trash[i] = True
    print(n-count)
