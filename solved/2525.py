a, b = [int(x) for x in input().split()]
c = int(input())
b += c % 60
a += c//60
if b >= 60:
    a += 1
    b -= 60
a %= 24

print(a, b)
