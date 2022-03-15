n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

seq = {}
for i in range(k):
    if seq.get(arr[i]) == None:
        seq[arr[i]] = []
    seq[arr[i]].append(i)

tab = [0]*n
ans = 0
for item in arr:
    done = False
    for i in range(n):
        if tab[i] == 0 or tab[i] == item:
            tab[i] = item
            done = True
            break
    if not done:
        selected_tab_idx = 0
        max_seq_idx = -1
        for i in range(n):
            item_in_tab = tab[i]
            if seq.get(item_in_tab) == None:
                selected_tab_idx = i
                break
            elif seq[item_in_tab][0] > max_seq_idx:
                max_seq_idx = seq[item_in_tab][0]
                selected_tab_idx = i
        tab[selected_tab_idx] = item
        ans += 1
    seq[item].pop(0)
    if len(seq[item]) == 0:
        del seq[item]

print(ans)
