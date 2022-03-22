n, m = [int(x) for x in input().split()]
truth = [int(x) for x in input().split()]
truth.pop(0)
parties = []
for _ in range(m):
    party = [int(x) for x in input().split()]
    party.pop(0)
    parties.append(party)

lie = [True for _ in range(len(parties))]
s = set()
for t in truth:
    s.add(t)

for _ in range(len(parties)+1):
    for i, party in enumerate(parties):
        can_lie = True
        for p in party:
            if p in s:
                can_lie = False
                break
        if not can_lie:
            for p in party:
                s.add(p)
            lie[i] = False

ans = 0
for l in lie:
    if l:
        ans += 1
print(ans)
# print(lie)
# print(s)
