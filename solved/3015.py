from collections import deque
import sys


n = int(input())
arr = []
for i in range(n):
    k = int(sys.stdin.readline().strip())
    if arr and k == arr[-1][0]:
        arr[-1][1] += 1
    else:
        arr.append([k, 1])


ans = 0
for i in range(len(arr)):
    ans += arr[i][1]*(arr[i][1]-1)//2

st = deque()
for i in range(len(arr)):
    tmp = 0
    while st:
        if st and st[-1][0] < arr[i][0]:
            ans += st[-1][1]
            st.pop()
        elif st and st[-1][0] == arr[i][0]:
            tmp += st[-1][1]
            ans += arr[i][1]*st[-1][1]
            st.pop()
        else:
            ans += arr[i][1]
            break
    st.append(arr[i])
    st[-1][1] += tmp

# print(st)
print(ans)
