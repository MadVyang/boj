d = {}
n = int(input())
for i in range(n):
    a, b, c = input().split()
    d[a] = (b, c)


def preorder(i):
    if i == '.':
        return ''
    s = i
    s += preorder(d[i][0])
    s += preorder(d[i][1])
    return s


def inorder(i):
    if i == '.':
        return ''
    s = inorder(d[i][0])
    s += i
    s += inorder(d[i][1])
    return s


def postorder(i):
    if i == '.':
        return ''
    s = postorder(d[i][0])
    s += postorder(d[i][1])
    s += i
    return s


print(preorder('A'))
print(inorder('A'))
print(postorder('A'))
