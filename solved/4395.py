n = int(input())
for _ in range(n):
    x, y = [int(x) for x in input().split()]
    d = y-x
    if d == 1:
        print(1)
        continue
    if d == 0:
        print(0)
        continue
    sum = 0
    i = 1
    while True:
        sum += i*2
        if sum < d and sum+i+1 >= d:
            print(i*2+1)
            break
        if sum >= d:
            print(i*2)
            break
        i += 1
