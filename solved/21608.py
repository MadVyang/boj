n = int(input())
arr = [[0]*n for _ in range(n)]

adjoints = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_empty_adjoints(y, x):
    result = []
    for dy, dx in adjoints:
        if y+dy >= 0 and y+dy < n and x+dx >= 0 and x+dx < n:
            if arr[y+dy][x+dx] == 0:
                result.append((y+dy, x+dx))
    return result


def get_adjoint_likes(y, x, likes):
    result = []
    for dy, dx in adjoints:
        if y+dy >= 0 and y+dy < n and x+dx >= 0 and x+dx < n:
            if arr[y+dy][x+dx] in likes:
                result.append((y+dy, x+dx))
    return result


all_likes = [[] for _ in range(n*n+1)]
# print(all_likes)
for _ in range(n*n):
    std = [int(x) for x in input().split()]
    me = std[0]
    likes = std[1:]
    all_likes[me] = likes

    max_adjoint_likes = 0
    max_empty_adjoints = 0
    min_i = 999
    min_j = 999
    selected = (-1, -1)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                adjoint_likes = get_adjoint_likes(i, j, likes)
                empty_adjoints = get_empty_adjoints(i, j)
                # print(me, i, j, adjoint_likes, max_adjoint_likes,
                #       empty_adjoints, max_empty_adjoints)
                if len(adjoint_likes) > max_adjoint_likes:
                    max_adjoint_likes = len(adjoint_likes)
                    max_empty_adjoints = len(empty_adjoints)
                    min_i = i
                    min_j = j
                    selected = (i, j)
                elif len(adjoint_likes) == max_adjoint_likes:
                    if len(empty_adjoints) > max_empty_adjoints:
                        max_empty_adjoints = len(empty_adjoints)
                        min_i = i
                        min_j = j
                        selected = (i, j)
                    elif len(empty_adjoints) == max_empty_adjoints:
                        if i < min_i:
                            min_i = i
                            min_j = j
                            selected = (i, j)
                        elif i == min_i:
                            if j < min_j:
                                min_j = j
                                selected = (i, j)
    arr[selected[0]][selected[1]] = me

# for i in range(n):
#     print(' '.join([str(x) for x in arr[i]]))

satisfcation = 0
for i in range(n):
    for j in range(n):
        adjoint_likes = get_adjoint_likes(i, j, all_likes[arr[i][j]])
        # print(adjoint_likes)
        if len(adjoint_likes) > 0:
            satisfcation += 10**(len(adjoint_likes)-1)
print(satisfcation)
