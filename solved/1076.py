a = input()
b = input()
c = input()

result = 0
if a == 'black':
    result += 0
elif a == 'brown':
    result += 1
elif a == 'red':
    result += 2
elif a == 'orange':
    result += 3
elif a == 'yellow':
    result += 4
elif a == 'green':
    result += 5
elif a == 'blue':
    result += 6
elif a == 'violet':
    result += 7
elif a == 'grey':
    result += 8
else:
    result += 9

result *= 10


if b == 'black':
    result += 0
elif b == 'brown':
    result += 1
elif b == 'red':
    result += 2
elif b == 'orange':
    result += 3
elif b == 'yellow':
    result += 4
elif b == 'green':
    result += 5
elif b == 'blue':
    result += 6
elif b == 'violet':
    result += 7
elif b == 'grey':
    result += 8
else:
    result += 9

if c == 'black':
    result *= 1
elif c == 'brown':
    result *= 10
elif c == 'red':
    result *= 100
elif c == 'orange':
    result *= 1000
elif c == 'yellow':
    result *= 10000
elif c == 'green':
    result *= 100000
elif c == 'blue':
    result *= 1000000
elif c == 'violet':
    result *= 10000000
elif c == 'grey':
    result *= 100000000
else:
    result *= 1000000000

print(result)
