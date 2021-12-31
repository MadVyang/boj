arr = []
for i in range(8):
    tmp = input()
    arr.append(tmp)
cnt = 0
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0 and arr[i][j] == 'F':
            cnt += 1
print(cnt)
