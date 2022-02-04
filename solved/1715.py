import heapq

n = int(input())
arr = []
for i in range(n):
    heapq.heappush(arr, int(input()))

sum = 0

while len(arr) > 1:
    addition = heapq.heappop(arr)+heapq.heappop(arr)
    sum += addition
    heapq.heappush(arr, addition)
print(sum)
# print(arr)
