N = int(input())

def check(n):
    count = 0
    while n>0:
        while n%10==6:
            count += 1
            n//=10
        if count >= 3:
            return True
        count = 0
        n//=10
    return False

num = 666
count = 0
while True:
    if check(num):
        count += 1
        if count == N:
            print(num)
            break
    num += 1
