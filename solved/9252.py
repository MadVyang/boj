a = '_'+input()
b = '_'+input()
la = len(a)
lb = len(b)

dp = []
for i in range(la):
    dp.append(['']*lb)
# for i in range(la):
#     if a[i] == b[1]:
#         dp[i][1] = a[i]
# for i in range(lb):
#     if a[0] == b[i]:
#         dp[0][i] = b[i]

for i in range(1, la):
    for j in range(1, lb):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1]+a[i]
        elif len(dp[i][j-1]) > len(dp[i-1][j]):
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = dp[i-1][j]

print(len(dp[la-1][lb-1]))
print(dp[la-1][lb-1])
