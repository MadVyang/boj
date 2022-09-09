a = int(input())
arr = [int(x) for x in input().split()]
count = 0
for i in arr:
    if i == a:
        count += 1
print(count)
