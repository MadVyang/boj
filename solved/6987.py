team = []
sim = [[0] * 3 for x in range(6)]


def check():
    for i in range(6):
        for j in range(3):
            if team[i][j] != sim[i][j]:
                return False
    return True


def dfs(a, b):
    if a == 5:
        for i in range(6):
            for j in range(3):
                if team[i][j] != sim[i][j]:
                    return False
        return True

    an = a
    bn = b + 1
    if bn == 6:
        an += 1
        bn = an + 1

    r1 = False
    r2 = False
    r3 = False

    if sim[a][0] < team[a][0] and sim[b][2] < team[b][2]:
        sim[a][0] += 1
        sim[b][2] += 1
        r1 = dfs(an, bn)
        sim[a][0] -= 1
        sim[b][2] -= 1

    if sim[a][1] < team[a][1] and sim[b][1] < team[b][1]:
        sim[a][1] += 1
        sim[b][1] += 1
        r2 = dfs(an, bn)
        sim[a][1] -= 1
        sim[b][1] -= 1

    if sim[a][2] < team[a][2] and sim[b][0] < team[b][0]:
        sim[a][2] += 1
        sim[b][0] += 1
        r3 = dfs(an, bn)
        sim[a][2] -= 1
        sim[b][0] -= 1

    return r1 or r2 or r3


ans = ''
for _ in range(4):
    arr = [int(x) for x in input().split()]
    team = []
    for i in range(6):
        team.append(arr[i * 3: i * 3 + 3])
    if dfs(0, 1):
        ans += '1 '
    else:
        ans += '0 '
print(ans)
