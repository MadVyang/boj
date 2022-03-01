from functools import cmp_to_key

n = int(input())
arr = [int(x) for x in input().split()]


def comparison(a, b):
    if int(str(a)+str(b)) > int(str(b)+str(a)):
        return -1
    return 1


arr.sort(key=cmp_to_key(comparison))
print(int(''.join([str(x) for x in arr])))
