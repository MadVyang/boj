import sys


t = int(input())
for i in range(t):
    arr = [int(x) for x in sys.stdin.readline().strip().split()]
    arr.sort()
    print(arr[-3])