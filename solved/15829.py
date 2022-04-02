l = int(input())
s = input()
h = 0
for i in range(l):
    h += int(ord(s[i])-ord('a')+1)*(31**i)
    h %= 1234567891
print(h)
