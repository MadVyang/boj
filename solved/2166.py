import sys


arr = []
n = int(input())
for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().strip().split()])


def triangle(a, b, c, d):
    return (a*d-b*c)/2


sum = 0
for i in range(1, n-1):
    sum += triangle(arr[0][0]-arr[i][0], arr[0][1]-arr[i][1],
                    arr[0][0]-arr[i+1][0], arr[0][1]-arr[i+1][1])
print(abs(sum))
