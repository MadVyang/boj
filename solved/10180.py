t = int(input())
for _ in range(t):
    n, d = [int(x) for x in input().split()]
    count = 0
    for i in range(n):
        v, f, c = [int(x) for x in input().split()]
        if f * v >= d*c:
            count += 1
    print(count)
