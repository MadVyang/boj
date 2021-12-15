N = int(input())
data = []
for i in range(N):
    data.append(list(map(int,input().split())))

team0= []
team1= []
min = 100000000000
def dfs():
    global min
    if len(team0)==N/2:
        team1 = [x for x in [i for i in range(N)] if x not in team0]
        s0 = cal(team0)
        s1 = cal(team1)
        if min>abs(s0-s1):
            min = abs(s0-s1)
        return
    last = 0
    if len(team0)>0:
        last = team0[-1]+1
    for i in range(last,N):
        team0.append(i)
        dfs()
        team0.pop(-1)


def cal(team):
    sum = 0
    for i in range(int(N/2)):
        for j in range(i+1,int(N/2)):
            sum += data[team[i]][team[j]]
            sum += data[team[j]][team[i]]
    return sum

dfs()

print(min)