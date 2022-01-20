n, k = [int(x) for x in input().split()]
arr = [x+1 for x in range(n)]
pivot = -1
s = '<'
while len(arr) > 0:
    pivot += k
    pivot %= len(arr)
    s += str(arr.pop(pivot))+', '
    pivot -= 1
s = s[0:len(s)-2]+'>'
print(s)
