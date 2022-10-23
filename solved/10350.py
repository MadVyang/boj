n = int(input())
arr = [int(x) for x in input().split()]*2
sm = [arr[0]]
for i in range(1, n*2):
    sm.append((sm[i-1]+arr[i]))

allsum = sum(arr[:n])
ans = 0

for i in range(n):
    for j in range(i, i+n):
        cur = sm[j]-sm[i]+arr[i]
        if cur < 0:
            cur = abs(cur)
            if cur % allsum != 0:
                ans += 1
            ans += cur//allsum
            # print(i, j, cur)
print(ans)
