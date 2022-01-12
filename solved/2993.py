s = input()
l = len(s)
ss = []

for i in range(1, l):
    for j in range(i+1, l):
        ss.append(s[0:i][::-1]+s[i:j][::-1]+s[j:l][::-1])
ss.sort()
print(ss[0])
