# a+bx=cx
# (c-b)x=a
# x=a/(c-b)

a,b,c = list(map(int, input().split()))

if c<=b:
    print(-1)
else:
    print(a//(c-b)+1)