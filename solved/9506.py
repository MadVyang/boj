n = int(input())
while n != -1:
    sum = 0
    arr = []
    for i in range(1, n):
        if n % i == 0:
            sum += i
            arr.append(i)
    if sum == n:
        s = str(n)+' = '
        for i in range(len(arr)):
            s += str(arr[i])+' '
            if i < len(arr)-1:
                s += '+ '
        print(s)
    else:
        print(str(n), 'is NOT perfect.')

    n = int(input())
