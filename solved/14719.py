from collections import deque


h, w = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
st = deque()
ans = 0
for i in range(w):
    acc = 0
    maxmin = 0
    count = 1
    while st and arr[st[-1][0]] < arr[i]:
        j, before_count = st.pop()
        maxmin = max(maxmin, arr[j])
        acc += (arr[i]-maxmin)*before_count
        count += before_count
    if not st:
        acc -= i*(arr[i]-maxmin)
    ans += acc
    # print(i, ans)
    st.append((i, count))

print(ans)
