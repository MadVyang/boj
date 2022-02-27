cow = [[] for i in range(26)]
for i, c in enumerate(input()):
    cow[ord(c)-ord('A')].append(i)
count = 0
for i in range(26):
    for j in range(i+1, 26):
        if cow[i][0] < cow[j][0] and cow[i][1] > cow[j][0] and cow[i][1] < cow[j][1]:
            count += 1
        elif cow[j][0] < cow[i][0] and cow[j][1] > cow[i][0] and cow[j][1] < cow[i][1]:
            count += 1
print(count)
