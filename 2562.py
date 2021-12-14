max = -1
index = -1
for i in range(9):
    n = int(input())
    if max<n:
        max = n
        index = i

print(max)
print(index+1)