import math


n = int(input())
exp = input()
ps = {i: 0 for i in range(n+1)}


def my_eval(exp):
    new_exp = []
    i = 0
    while i < len(exp):
        if exp[i] == '(':
            new_exp.append(eval(exp[i:i+5]))
            i += 4
        else:
            new_exp.append(exp[i])
        i += 1
    r = int(new_exp[0])
    for i in range(1, len(new_exp), 2):
        if new_exp[i] == '*':
            r *= int(new_exp[i+1])
        elif new_exp[i] == '+':
            r += int(new_exp[i+1])
        else:
            r -= int(new_exp[i+1])
    return r


def cal():
    new_exp = ''
    for i in range(n):
        if ps[i] == 1:
            new_exp += '('
        elif ps[i] == -1:
            new_exp += ')'
        new_exp += exp[i]
    if ps[n] == -1:
        new_exp += ')'
    # print(new_exp)
    return my_eval(new_exp)


def solve(i):
    global n
    if i > n-1:
        return cal()
    mx = -math.inf
    mx = max(solve(i+1), mx)
    if i % 2 == 0 and i < n-2:
        ps[i] = 1
        ps[i+3] = -1
        mx = max(solve(i+3), mx)
        ps[i+3] = 0
        ps[i] = 0
    return mx


print(solve(0))
