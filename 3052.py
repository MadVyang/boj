count = dict()
for i in range(10):\
    count[int(input())%42]=True
print(len(count.keys()))