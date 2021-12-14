N = int(input())

mem = [0,1,1,1,2,2,3,4,5,7,9]

for i in range(11,101):
    mem.append(mem[i-1]+mem[i-5])

for i in range(N):
    n = int(input())
    print(mem[n])

# 4 = 3+1
# 5 = 4+1
# 7 = 5+2
# 9 = 7+2  i = i-1 + i-
# 12 = 9+3
# 16 = 12+4
#