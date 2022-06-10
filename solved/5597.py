s = set()
for i in range(28):
    s.add(int(input()))
for i in range(1, 31):
    if i not in s:
        print(i)
