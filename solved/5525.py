n = int(input())
m = int(input())
s = input()

count = 0
clen = 0
for i in range(1, m-1):
    if s[i] == 'O':
        if s[i-1] == 'I' and s[i+1] == 'I':
            clen += 1
            if clen >= n:
                count += 1
                # print(s[:i+1])
        else:
            clen = 0
    elif s[i-1] == 'I':
        clen = 0

print(count)
