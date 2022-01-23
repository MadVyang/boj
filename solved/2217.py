n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
ans = 0
for i in range(n):
    t = arr[i]*(i+1)
    if ans < t:
        ans = t
print(ans)
