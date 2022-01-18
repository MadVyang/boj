n = int(input())
abc = [0]*10
firsts = []
for _ in range(n):
    s = input()
    for i in range(len(s)):
        c = ord(s[len(s)-1-i])-ord('A')
        abc[c] += 10**i
    if ord(s[0]) not in firsts:
        firsts.append(ord(s[0])-ord('A'))
# print(firsts)

sel = []
unsel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt = 0


def genf():
    global cnt

    if len(unsel) == 0:
        cnt += 1
        solve()
    for k in range(len(unsel)):
        t = unsel[k]
        if t == 0 and len(sel) in firsts:
            continue
        sel.append(t)
        unsel.pop(k)
        genf()
        sel.pop()
        unsel.insert(k, t)


mx = 0


def solve():
    global mx
    cur = 0
    for i in range(10):
        cur += abc[i]*sel[i]
    if cur > mx:
        mx = cur


genf()
print(mx)
