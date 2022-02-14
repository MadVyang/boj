def get_num(nums):
    result = 0
    for i in nums:
        result *= 10
        result += i
    return result


def get_clock_num(nums):
    _nums = nums.copy()
    for i in nums:
        _nums.append(i)
    mn = 10000
    for i in range(4):
        cur = get_num(_nums[i:i+4])
        if cur < mn:
            mn = cur
    return mn


test = get_clock_num([int(x) for x in input().split()])

clock_nums = []
selected = []

visited = [False]*10000


def gen(i):
    if len(selected) == 4:
        clock_num = get_clock_num(selected)
        if not visited[clock_num]:
            visited[clock_num] = True
            clock_nums.append(clock_num)
        return
    for i in range(1, 10):
        selected.append(i)
        gen(i)
        selected.pop()


for i in range(1, 10):
    gen(i)
# print((clock_nums))

for i in range(len(clock_nums)):
    if test == clock_nums[i]:
        print(i+1)
        break
