a = {
    4: 'E',
    3: 'A',
    2: 'B',
    1: 'C',
    0: 'D'
}
for i in range(3):
    print(a[sum([int(x) for x in input().split()])])
