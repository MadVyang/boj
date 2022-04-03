def check(s):
    q = []
    for c in s:
        if c == '(':
            q.append(c)
        if c == ')':
            if len(q) > 0 and q[-1] == '(':
                q.pop()
            else:
                return False
        if c == '[':
            q.append(c)
        if c == ']':
            if len(q) > 0 and q[-1] == '[':
                q.pop()
            else:
                return False
    return len(q) == 0


while True:
    s = input()
    if s == '.':
        break
    if check(s):
        print('yes')
    else:
        print('no')
