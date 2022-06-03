from collections import deque
import sys


while True:
    arr = [int(x) for x in sys.stdin.readline().strip().split()]
    n = arr[0]
    if n == 0:
        break
    arr = arr[1:]

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
