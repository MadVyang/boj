import string


def min_k(count, l, k):
    min_len = l+1
    for c in string.ascii_lowercase:
        for i in range(k-1, len(count[c])):
            min_len = min(min_len, count[c][i]-count[c][i-(k-1)]+1)
    if min_len > l:
        return -1
    return min_len


def max_k(count, w, k):
    max_len = -1
    for c in string.ascii_lowercase:
        for i in range(k-1, len(count[c])):
            max_len = max(max_len, count[c][i]-count[c][i-(k-1)]+1)
    return max_len


t = int(input())
for _ in range(t):
    w = input()
    l = len(w)
    k = int(input())

    count = {x: [] for x in string.ascii_lowercase}
    for i in range(l):
        count[w[i]].append(i)

    ans1 = min_k(count, l, k)
    ans2 = max_k(count, w, k)
    if ans1 > 0 and ans2 > 0:
        print(ans1, ans2)
    else:
        print(-1)
