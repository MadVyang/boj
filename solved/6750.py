a = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']

ans = 'YES'
for s in input():
    if s not in a:
        ans = 'NO'
print(ans)