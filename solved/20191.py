import string

s = input()
t = input()
tmap = {}
for c in string.ascii_lowercase:
    tmap[c] = []
for i in range(len(t)):
    tmap[t[i]].append(i)

si = 0
ans = 1
ti = -1
while si < len(s):
    tis = tmap[s[si]]
    if len(tis) == 0:
        ans = -1
        break

    left = 0
    right = len(tis)-1
    while left < right:
        mid = (left+right)//2
        if tis[mid] > ti:
            right = mid
        else:
            left = mid+1

    if tis[right] > ti:
        si += 1
        ti = tis[right]
    else:
        ans += 1
        ti = -1

print(ans)
