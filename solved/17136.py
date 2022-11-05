bd = []
num_one = 0
for i in range(10):
    tmp = [int(x) for x in input().split()]
    num_one += sum(tmp)
    bd.append(int('0b'+''.join([str(x) for x in tmp]), 2))


check_s = {}
for j in range(10):
    for size in range(1, 11):
        if j+size > 10:
            continue
        s = '0b'
        s += '0'*j
        s += '1'*size+'0'*(10-j-size)
        s = int(s, 2)
        check_s[(j, size)] = s

fill_s = {}
for j in range(10):
    for size in range(1, 11):
        if j+size > 10:
            continue
        s = '0b'
        s += '1'*j
        s += '0'*size+'1'*(10-j-size)
        s = int(s, 2)
        fill_s[(j, size)] = s


def check(i, j, size):
    if i < 0 or j < 0 or i+size > 10 or j+size > 10:
        return False
    s = check_s[(j, size)]
    for ii in range(i, i+size):
        if bd[ii] & s != s:
            return False
        # for jj in range(j, j+size):
        #     if bd[ii][jj] == 0:
        #         return False
    return True


def fill(i, j, size, color):
    s = fill_s[(j, size)]
    for ii in range(i, i+size):
        bd[ii] = bd[ii] & s
        # for jj in range(j, j+size):
        #     bd[ii][jj] = color


remains = [0, 5, 5, 5, 5, 5]
ans = 26

# if check(0, 0, 10):
#     remains[5] -= 4
#     fill(0, 0, 10, 0)
#     num_one = 0
# for i in range(2):
#     for j in range(2):
#         if check(i, j, 8):
#             mm = 64
#             for di, dj in [(-1,-1), (-1,4), (4,-1), (4,4)]:
#                 if check(i+di, j+dj, 5):
#                     fill(i+di, j+dj, 5)
#                     remains[5] -= 1
#                     mm -= 25
#             fill(i, j, 8)
#             num_one -= mm
#             break


def dfs(si, sj):
    global ans, remains, num_one
    cur_ans = 25-sum(remains)
    if num_one == 0:
        ans = min(cur_ans, ans)
        return
    if cur_ans > ans:
        return
    # print(si, sj, sk, num_one)
    # print(remains)
    # for r in bd:
    #     s = bin(r)[2:]
    #     s = '0'*(10-len(s))+s
    #     print(s)

    # poten = 0
    # for k in range(1, sk+1):
    #     poten += remains[k]*k*k
    # if poten < num_one:
    #     return

    for i in range(si, 10):
        for j in range(sj, 10):
            if (bd[i] & (1 << (10-j-1))) == (1 << (10-j-1)):
                for k in range(5, 0, -1):
                    if remains[k] == 0:
                        si, sj = 0, 0
                        continue
                    if check(i, j, k):
                        ni, nj = i, j+1
                        if j == 10:
                            nj = 0
                            ni = i+1

                        tmp = bd[i:i+k]

                        fill(i, j, k, 0)
                        num_one -= k*k
                        remains[k] -= 1

                        dfs(ni, nj)

                        for ii in range(i, i+k):
                            bd[ii] = tmp[ii-i]
                        # fill(i, j, k, 1)
                        num_one += k*k
                        remains[k] += 1
                return
            sj = 0
        si, sj = 0, 0


dfs(0, 0)
if ans > 25:
    ans = -1
print(ans)
