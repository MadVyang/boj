n = int(input())
arr = [int(input()) for x in range(n)]


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


g = abs(arr[0]-arr[1])
for i in range(n):
    for j in range(i+1, n):
        g = gcd(abs(arr[i]-arr[j]), g)


ans = set()
for i in range(1, g+1):
    if i*i > g:
        break
    if g % i == 0:
        ans.add(i)
        ans.add(g//i)
ans = [i for i in ans]
ans.sort()
ans = [str(i) for i in ans]
print(' '.join(ans[1:]))
