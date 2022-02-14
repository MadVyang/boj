arr = [[0]*120 for i in range(120)]
for _ in range(4):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

count = 0
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            count += 1
print(count)

# for i in range(1, 10):
#     print(arr[i][1:10])
