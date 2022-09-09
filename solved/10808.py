import string


s = input()
d = {}
for i in string.ascii_lowercase:
    d[i] = 0
for i in s:
    d[i] += 1

s = ''
for i in d:
    s += str(d[i])+' '
print(s)
