import sys


n, m = [int(x) for x in input().split()]
arr = ['']
dct = {}
for i in range(n):
    arr.append(sys.stdin.readline().strip())
    dct[arr[-1]] = i+1

for i in range(m):
    q = sys.stdin.readline().strip()
    try:
        print(dct[q])
    except:
        print(arr[int(q)])
