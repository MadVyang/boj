import sys


sys.setrecursionlimit(10**6)

class Node:
    def __init__(self):
        self.v = 0
        self.left = None
        self.right = None


nums = [int(x) for x in sys.stdin.readlines()]


def solve(root, start, end):
    if start >= len(nums):
        return
    root.v = nums[start]
    if start >= end:
        return

    left = start
    for i in range(start+1, end+1):
        if nums[i] < root.v:
            left = i

    root.left = Node()
    root.right = Node()
    if left > start:
        solve(root.left, start+1, left)
    if left < end:
        solve(root.right, left+1, end)


root = Node()
solve(root, 0, len(nums)-1)


# print(arr[1:len(nums*5)])


def traverse(root):
    if not root or root.v == 0:
        return
    traverse(root.left)
    traverse(root.right)
    print(root.v)


traverse(root)
