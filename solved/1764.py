import sys


n,m = [int(x) for x in sys.stdin.readline().strip().split()]
a = set()
b=set()
for i in range(n):
    a.add(sys.stdin.readline().strip())
for i in range(m):
    b.add(sys.stdin.readline().strip())
c = [i for  i in a&b]
c.sort()
print(len(c))
print('\n'.join(c))
