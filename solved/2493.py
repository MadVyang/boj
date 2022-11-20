from collections import deque


n = int(input())
arr = [int(x) for x in input().split()]

ans = [0]*n
st = deque()
for i in range(n-1, -1, -1):
    if st:
        while st and arr[i] > arr[st[-1]]:
            ans[st[-1]] = i+1
            st.pop()
        pass
    st.append(i)

print(' '.join([str(x) for x in ans]))
