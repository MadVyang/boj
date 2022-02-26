n = int(input())
mem = {}
count = 0
for i in range(n):
    a, b = [int(x) for x in input().split()]
    if mem.get(a) != None and mem[a] != b:
        count += 1
    mem[a] = b
print(count)
