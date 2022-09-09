from collections import deque
import sys


sys.setrecursionlimit(10**6)

s = input()
b = input()


st = []
for i in range(len(s)):
    st.append(s[i])

    # print(st[-len(b)-1:-1])
    if st[-1] == b[-1] and ''.join(st[-len(b):]) == b:
        [st.pop() for _ in range(len(b))]

s = ''.join(st)
if s == '':
    s = 'FRULA'
print(s)
