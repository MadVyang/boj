n = int(input())


def check(s):
    l = len(s)
    for i in range(1, l//2+1):
        if s[-i*2:-i] == s[-i:]:
            return False
    return True


def solve(s, i):
    global n
    l = len(s)
    if l == n:
        return s

    for j in range(1, 4):
        if i == j:
            continue
        ss = s+str(j)
        if check(ss):
            r = solve(ss, j)
            if r != '':
                return r
    return ''


s = solve('', -1)
print(s)
