from collections import deque


n = int(input())
arr = [int(x) for x in input().split()]
st = deque([(arr[0], 0)])
ans = [-1]*n
for i in range(1, n):
    if st and arr[i] > st[-1][0]:
        while st and st[-1][0] < arr[i]:
            ans[st[-1][1]] = arr[i]
            st.pop()
    st.append((arr[i], i))

print(' '.join([str(x) for x in ans]))
