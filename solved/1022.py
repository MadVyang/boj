r1, c1, r2, c2 = [int(x) for x in input().split()]


def solve(r, c):
    if r == 0 and c == 0:
        return 1

    shell = max(abs(r), abs(c))
    size = shell*2+1

    if r < 0 and abs(r) == shell:
        mid = (size-2)**2+size-1+size//2
        return mid-c
    if r > 0 and abs(r) == shell:
        mid = size**2-size//2
        return mid+c
    if c < 0 and abs(c) == shell:
        mid = ((size-2)**2+size**2)//2+size//2
        return mid+r
    if c > 0 and abs(c) == shell:
        mid = (size-2)**2+size//2
        return mid-r
    return 0


result = []
mxlen = 0
for r in range(r1, r2+1):
    line = []
    for c in range(c1, c2+1):
        num = str(solve(r, c))
        mxlen = max(mxlen, len(num))
        line.append(num)
    result.append(line)

for line in result:
    s = ''
    for c in line:
        while len(c) < mxlen:
            c = ' '+c
        s += c+' '
    print(s)
