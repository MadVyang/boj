import sys


n = int(input())
arr = [int(sys.stdin.readline().strip()) for x in range(n)]
arr.sort(reverse=True)
sarr = set()
for i in arr:
    for j in arr:
        sarr.add(i+j)
sarr = list(sarr)
sarr.sort()
# print(sarr)
# ans = 0
for i in range(n):
    for j in range(i, n):
        t = arr[i]-arr[j]
        left, right = 0, len(sarr)-1
        while left <= right:
            mid = (left+right)//2
            if sarr[mid] == t:
                print(arr[i])
                exit()
            elif sarr[mid] < t:
                left = mid+1
            else:
                right = mid-1
# print(ans)
