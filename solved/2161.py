n = int(input())
arr = [x+1 for x in range(n)]
s = ''
while len(arr) > 1:
    s += str(arr[0])+' '
    arr.pop(0)
    t = arr.pop(0)
    arr.append(t)
s += str(arr[0])
print(s)
