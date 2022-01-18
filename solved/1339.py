n = int(input())
abc = {}
for _ in range(n):
    s = input()
    for i in range(len(s)):
        c = s[len(s)-1-i]
        if c not in abc:
            abc[c] = 0
        abc[c] += 10**i
# print(abc)

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
        sel.append(t)
        unsel.pop(k)
        genf()
        sel.pop()
        unsel.insert(k, t)


mx = 0


def solve():
    global mx
    cur = 0
    arr = [x for x in abc.values()]
    while len(arr) < 10:
        arr.append(0)
    for i in range(10):
        cur += arr[i]*sel[i]
    if cur > mx:
        mx = cur


genf()
print(mx)
