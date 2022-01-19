import re
s = input()
p = re.compile(r'((100+1+)|(01))+')
m = p.fullmatch(s)
if m == None:
    print('NOISE')
else:
    print('SUBMARINE')
