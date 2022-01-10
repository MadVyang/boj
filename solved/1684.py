n = int(input())
nums = [int(x) for x in input().split()]
nums.sort(reverse=True)

mx = max(abs(nums[0]), abs(nums[n-1]))+1
for d in range(mx, 0, -1):
    check = True
    r = nums[0] % d
    for i in nums:
        if i % d != r:
            check = False
            break
    if check:
        print(d)
        break
