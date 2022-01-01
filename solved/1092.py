n = int(input())
cr = [int(x) for x in input().split()]
m = int(input())
box = [int(x) for x in input().split()]

cr.sort(reverse=True)
box.sort(reverse=True)
# print(cr, box)
cnt = 0
while len(box) > 0:
    k = 0
    i = 0
    while i < n and len(box) > k:
        b = box[k]
        # print(i, k, b)
        if b <= cr[i]:
            i += 1
            box.pop(k)
            if len(box) == 0:
                break
        else:
            # i -= 1
            k += 1
            if k >= len(box):
                break
    # print(box)
    cnt += 1
    if cnt > 10000:
        cnt = -1
        break

print(cnt)
