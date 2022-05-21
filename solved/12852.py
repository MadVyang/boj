from collections import deque


n = int(input())
q = deque([(n, 0)])
while q:
    i, c = q.popleft()
    if i == 1:
        break
    if i % 3 == 0:
        q.append((i//3, c+1))
    if i % 2 == 0:
        q.append((i//2, c+1))
    q.append((i-1, c+1))

print(c)

hist = [n]

solved = False


def solve(n):
    global c, solved
    if solved:
        return False
    if len(hist) == c+1:
        if n == 1:
            solved = True
            print(' '.join(str(x) for x in hist))
            return True
        else:
            return False
    if n % 3 == 0:
        hist.append(n//3)
        if solve(n//3):
            return
        hist.pop()
    if n % 2 == 0:
        hist.append(n//2)
        if solve(n//2):
            return
        hist.pop()
    hist.append(n-1)
    if solve(n-1):
        return
    hist.pop()


solve(n)
