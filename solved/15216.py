h, w, n = map(int, input().split())
arr = [int(x) for x in input().split()]
cur_h = 0
cur_w = 0
for i in range(n):
    cur_w += arr[i]
    if cur_w > w:
        print('NO')
        exit()
    if cur_w == w:
        cur_h += 1
        cur_w = 0
        if cur_h == h:
            print('YES')
            exit()
# print(cur_h)
