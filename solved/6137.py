from collections import deque


n = int(input())
s = [input() for i in range(n)]

t = []
i, j = 0, n-1
count = 0
while count < n:
    count += 1
    if s[i] < s[j]:
        t.append(s[i])
        i += 1
    elif s[j] < s[i]:
        t.append(s[j])
        j -= 1
    else:
        solved = False
        for k in range(1, n):
            if i+k > j-k:
                break
            if s[i+k] < s[j-k]:
                t.append(s[i])
                i += 1
                solved = True
                break
            elif s[i+k] > s[j-k]:
                t.append(s[j])
                j -= 1
                solved = True
                break
        if not solved:
            t.append(s[i])
            i += 1
    if len(t) == 80:
        print(''.join(t))
        t = []

if len(t) > 0:
    print(''.join(t))
