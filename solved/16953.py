a, b = [int(x) for x in input().split()]
count = 0
while True:
    count += 1
    if b == a:
        break
    if b < a:
        count = -1
        break
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        count = -1
        break
print(count)

# def dfs(current, count):
#     global a, b
#     if current == b:
#         return count
#     if current > b:
#         return 123456789
#     return min(dfs(current * 2, count + 1), dfs(current * 10 + 1, count + 1))


# ans = dfs(a, 0) + 1
# if ans >= 123456789:
#     ans = -1
# print(ans)

