s = input()
for i in range(len(s)):
    if s[i] in ['+', '-', '/', '*']:
        if i == 0 or s[i-1] in ['+', '-', '/', '*', '(']:
            print('ROCK')
            exit()
        if i == len(s) or s[i+1] in ['+', '-', '/', '*', ')']:
            print('ROCK')
            exit()
s = s.replace('/', '//')
try:
    print(int(eval(s)))
except:
    print('ROCK')
