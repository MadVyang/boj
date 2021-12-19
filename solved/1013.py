import re

n = int(input())
for i in range(n):
    s = input()
    result = re.compile('((100+1+)|(01))+').fullmatch(s)
    if not result:
        print('NO')
    else:
        print('YES')
