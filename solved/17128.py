n, q = [int(x) for x in input().split()]
scores = [int(x) for x in input().split()]
# scores.insert(0, 0)

sum = 0
for i in range(n):
    mul = scores[i]
    for j in range(1, 4):
        mul *= scores[(i+j) % n]
    sum += mul
# print(sum)

for i in [int(x) for x in input().split()]:
    i -= 1
    start_i = i+n-3

    for k in range(4):
        mul = scores[(start_i+k) % n]
        for j in range(1, 4):
            mul *= scores[(start_i+k+j) % n]
        sum -= mul

    scores[i] *= -1

    for k in range(4):
        mul = scores[(start_i+k) % n]
        for j in range(1, 4):
            mul *= scores[(start_i+k+j) % n]
        sum += mul

    # print(scores)
    print(sum)
