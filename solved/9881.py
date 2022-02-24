n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
mn = 123456789
for r in range(0, 101-17):
    sum = 0
    for i in arr:
        if i < r:
            sum += (r-i)**2
        elif i > r+17:
            sum += (i-r-17)**2
    mn = min(mn, sum)
print(mn)
