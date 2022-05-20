from collections import deque
import sys


n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

st = deque([(0, arr[0])])
mx = 0
for i in range(1, n):
    ii = i
    while st and st[-1][1] > arr[i]:
        ii = st[-1][0]
        mx = max(mx, (i-st[-1][0])*st[-1][1])
        st.pop()
    st.append((ii, arr[i]))
while st:
    i, h = st.pop()
    mx = max(mx, (n-i)*h)
print(mx)
