import sys


n, c = map(int, input().split())
arr = [int(sys.stdin.readline().strip()) for x in range(n)]
arr.sort()
mm = arr[1]-arr[0]
for i in range(1, n):
    mm = min(mm, arr[i]-arr[i-1])


def check(dist):
    current_dist = 0
    count = 1
    for i in range(1, n):
        current_dist += arr[i]-arr[i-1]
        if current_dist >= dist:
            current_dist = 0
            count += 1
    return count >= c


l, h = mm, arr[n-1]-arr[0]+1

while l < h:
    m = (l+h)//2
    if check(m):
        l = m+1
    else:
        h = m

print(h-1)
