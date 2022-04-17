import sys


n, m = [int(x) for x in sys.stdin.readline().strip().split()]
arr = [int(x) for x in sys.stdin.readline().strip().split()]
sum = [arr[0]]
for i in range(1, n):
    sum.append(arr[i]+sum[i-1])
for _ in range(m):
    i, j = [int(x) for x in sys.stdin.readline().strip().split()]
    i -= 1
    j -= 1
    print(sum[j]-sum[i]+arr[i])
