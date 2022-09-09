t = {
    '000': 0,
    '001': 1,
    '010': 2,
    '100': 4,
    '011': 3,
    '101': 5,
    '110': 6,
    '111': 7,
}

a = input()
p = len(a) % 3
ans = ''
if p > 0:
    tmp = a[0:p]
    for i in range(3-p):
        tmp = '0'+tmp
    ans += str(t[tmp])

for i in range(p, len(a), 3):
    ans += str(t[a[i:i+3]])
print(ans)
