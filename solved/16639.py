import math


n = int(input())
exp = input()
nums = [int(exp[i]) for i in range(n) if i % 2 == 0]
ops = [exp[i] for i in range(n) if i % 2 == 1]
n = n//2+1


def solve():
    if len(ops) == 0:
        return nums[0]
    mx = -math.inf
    for i in range(len(ops)):
        num1 = nums[i]
        num2 = nums[i+1]
        op = ops[i]
        r = num1
        if op == '*':
            r *= num2
        elif op == '+':
            r += num2
        else:
            r -= num2
        nums.pop(i)
        nums.pop(i)
        ops.pop(i)
        nums.insert(i, r)
        mx = max(mx, solve())
        nums.pop(i)
        nums.insert(i, num2)
        nums.insert(i, num1)
        ops.insert(i, op)
    return mx


print(solve())
