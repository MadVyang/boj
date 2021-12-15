N = int(input())
mem = []
for i in range(10):
    mem.append([0]*101)

for i in range(1,10):
    mem[i][1] = 1

for i in range(2,101):
    for j in range(10):
        if 1<=j<=8:
            mem[j][i] = mem[j-1][i-1] + mem[j+1][i-1]
        elif j==0:
            mem[j][i] = mem[j+1][i-1]
        else:
            mem[j][i] = mem[j-1][i-1]
        
_sum = 0
for i in range(10):
    _sum+=mem[i][N]
    # print(mem[i][N])

print(_sum % 1000000000)