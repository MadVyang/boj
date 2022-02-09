first = int(input())
mx = 0
mx_nums = []
for i in range(1, first+1):
    nums = [first]
    cur = first
    next = i
    while next >= 0:
        nums.append(next)
        next = cur - next
        cur = nums[-1]
    if len(nums) > mx:
        mx = len(nums)
        mx_nums = nums.copy()
print(mx)
print(' '.join([str(x) for x in mx_nums]))
