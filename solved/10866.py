from collections import deque
import sys

q = deque()
n = int(input())
for _ in range(n):
    line = sys.stdin.readline().strip().split()
    cmd = line[0]
    if cmd == 'push_back':
        q.append(line[1])
    elif cmd == 'push_front':
        q.appendleft(line[1])
    elif cmd == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif cmd == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif cmd == 'front':
        if len(q) == 0:
            print(-1)
        else:
            a = q.popleft()
            print(a)
            q.appendleft(a)
    elif cmd == 'back':
        if len(q) == 0:
            print(-1)
        else:
            a = q.pop()
            print(a)
            q.append(a)
    elif cmd == 'size':
        print(len(q))
    else:
        if len(q) == 0:
            print(1)
        else:
            print(0)
