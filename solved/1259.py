while True:
    n = input()
    if n == '0':
        break
    r = 'yes'
    for i in range(len(n)):
        if n[i] != n[len(n)-i-1]:
            r = 'no'
            break
    print(r)
