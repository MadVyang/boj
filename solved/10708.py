N = int(input())
M = int(input())
target = [int(x)-1 for x in input().split()]
score = []
for i in range(N):
    score.append(0)
for i in range(M):
    game = [int(x)-1 for x in input().split()]
    for j in range(N):
        if game[j] == target[i]:
            score[j] += 1
        else:
            score[target[i]] += 1

for i in range(N):
    print(score[i])
