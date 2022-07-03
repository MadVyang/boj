import sys


arr = [0]*10001

nums = [int(x) for x in sys.stdin.readlines()]


pos = 0


def get(cur):
    global pos
    arr[cur] = nums[pos]
    print(arr[cur], cur, pos)
    pos += 1
    if pos == len(nums):
        return
    if arr[cur] > nums[pos]:
        a = get(cur*2)
    else:
        get(cur*2+1)


get(1)

print(arr[1:pos])
