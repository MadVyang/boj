n = int(input())
car = {}
for i in range(n):
    car[input()] = i
arr = []
for i in range(n):
    arr.append(car[input()])

# dp = [0]*n
# for i in range(n):
#     dp[i] = 1
#     for j in range(i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(n-max(dp))

ans = 0
for i in range(n):
    for j in range(i, n):
        if arr[i] > arr[j]:
            ans += 1
            break
print(ans)
