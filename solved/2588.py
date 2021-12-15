n1 = int(input())
n2 = int(input())
_n2=n2

for i in range(3):
    print(n1*(n2%10))
    n2//=10
print(n1*_n2)