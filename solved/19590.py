n = int(input())
arr = []
mx = 0
sum = 0
for i in range(n):
    xi = int(input())
    arr.append(xi)
    if mx < xi:
        mx = xi
    sum += xi
if sum-mx < mx:
    print(mx-(sum-mx))
else:
    print(sum % 2)
