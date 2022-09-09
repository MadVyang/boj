k = int(input())
for i in range(k):
    n, m = map(int, input().split())
    routes = {}
    for j in range(m):
        routes[j] = set([int(x) for x in input().split()])
    current = set([1])

    ans = []
    for jj in range(m):
        found = False
        for j in routes:
            # print(routes[j] & current)
            if current & routes[j]:
                ans.append(j+1)
                current = current | routes[j]
                routes.pop(j)
                found = True
                break
        if not found:
            ans = []
            # print(routes)
            # print(current)
            break

    print(f'Data Set {i+1}:')
    if ans:
        print('\n'.join([str(x) for x in ans]))
    else:
        print('Impossible')
    print()
