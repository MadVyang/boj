arr = [int(x) for x in input().split()]

tr = {str(i*2): [str(i*2+j*2) if i*2+j*2 <= 40 else '50' for j in range(1, 6)] for i in range(21)}
tr['10'] = ['13', '16 ', '19', '25', '30 ']
tr['13'] = ['16 ', '19', '25', '30 ', '35']
tr['16 '] = ['19', '25', '30 ', '35', '40']
tr['19'] = ['25', '30 ', '35', '40', '50']

tr['20'] = ['22 ', '24 ', '25', '30 ', '35']
tr['22 '] = ['24 ', '25', '30 ', '35', '40']
tr['24 '] = ['25', '30 ', '35', '40', '50']

tr['30'] = ['28 ', '27', '26 ', '25', '30 ']
tr['28 '] = ['27', '26 ', '25', '30 ', '35']
tr['27'] = ['26 ', '25', '30 ', '35', '40']
tr['26 '] = ['25', '30 ', '35', '40', '50']

tr['25'] = ['30 ', '35', '40', '50', '50']
tr['30 '] = ['35', '40', '50', '50', '50']
tr['35'] = ['40', '50', '50', '50', '50']

tr['50'] = []

# for i in tr:
#     print(i, tr[i])


ps = {i: 0 for i in tr}
ps['0'] = 4


def dfs(i, s: set):
    if i == 10:
        return 0
    mx = 0
    for p in s:
        n = tr[p][arr[i]-1]
        if n in s:
            continue

        ns = s.copy()

        ps[p] -= 1
        ps[n] += 1

        if ps[p] == 0:
            ns.remove(p)
        if n != '50':
            ns.add(n)
            mx = max(mx, int(n)+dfs(i+1, ns))
        else:
            mx = max(mx, dfs(i+1, ns))

        ps[n] -= 1
        ps[p] += 1
    return mx


s = set(['0'])
print(dfs(0, s))
