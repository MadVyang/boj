n = int(input())
arr = [True]*(n+1)
for i in range(4, n+1):
    if i*i > n:
        break
    for j in range(i*2, n+1, i):
        arr[j] = False
p = [2, 3]
for i in range(5, n+1):
    if i % 2 != 0 and i % 3 != 0 and arr[i]:
        p.append(i)

l = len(p)
s = [p[0]]
for i in range(1, l):
    s.append(s[i-1]+p[i])

ans = 0
for i in range(l):
    if s[i] == n:
        ans += 1
    if p[i] > n:
        break
    low, high = i, l-1
    while low <= high:
        mid = (low+high)//2
        if s[mid]-s[i] < n:
            low = mid+1
        elif s[mid]-s[i] > n:
            high = mid-1
        else:
            ans += 1
            break
print(ans)
