n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

mem = [0]*(k+1)
for i in range(n):
    for j in range(k+1):
        if j-arr[i] < 0:
            continue
        if arr[i] == j:
            mem[j] += 1
        else:
            mem[j] = mem[j]+mem[j-arr[i]]
print(mem[k])
