n, m = [int(x) for x in input().split()]

mem = []
for i in range(0, 101):
    mem.append([])

mem[0] = [0]
mem[1] = [1, 1]
mem[2] = [1, 2, 1]
# print(mem)

for i in range(3, 101):
    mem[i].append(1)
    for j in range(1, i):
        mem[i].append(mem[i-1][j]+mem[i-1][j-1])
    mem[i].append(1)
    # print(mem[i])


# def comb(a, b):
print(mem[n][m])
