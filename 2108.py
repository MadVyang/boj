import sys

N = int(input())
nums = []
sum = 0
min = 999999
max = -9999999
count = []
for i in range(10000):
    count.append([i,0])

for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    sum += n
    if n<min:
        min = n
    if n>max:
        max = n
    nums.append(n)
    count[n+4000][1]+=1

# 1
print(round(sum/N))

nums.sort()

# 2
print(nums[N//2])

# 3
count.sort(key=lambda x: x[1],reverse=True)
candi = [count[0][0]-4000]
for i in range(1,10000):
    if count[0][1] == count[i][1]:
        candi.append(count[i][0]-4000)
    else:
        break
candi.sort()
if len(candi)>1:
    print(candi[1])
else:
    print(candi[0])

# 4
print(max - min)