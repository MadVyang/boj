arr = []
for i in range(1, 46):
    for j in range(i):
        arr.append(i)

a, b = map(int, input().split())
# print(arr, arr[a-1:b])
s = 0
for k in arr[a-1:b]:
    s += k
print(s)
