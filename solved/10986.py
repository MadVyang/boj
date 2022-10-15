n, m = map(int, input().split())
arr = [int(x) for x in input().split()]
remain = {0: 1}
s = 0
for i in range(n):
    s += arr[i]
    if (s % m) not in remain:
        remain[s % m] = 0
    remain[s % m] += 1

ans = 0
for i in remain:
    ans += remain[i]*(remain[i]-1)//2
print(ans)
