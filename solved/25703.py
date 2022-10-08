n = int(input())
print('int a;')
print('int *ptr = &a;')
for i in range(1, n):
    s = '*'*(i+1)
    a = str(i+1)
    b = str(i)
    if i == 1:
        b = ''
    print(f'int {s}ptr{a} = &ptr{b};')
