s = ''
for c in input():
    if c.lower() == c:
        s += c.upper()
    else:
        s += c.lower()
print(s)
