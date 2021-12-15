N = int(input())
nums = map(int,input().split())
max = -1000001
min = 1000001
for n in nums:
    if n<min:
        min = n
    if n>max:
        max =n
print(min,max)