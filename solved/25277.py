n = int(input())
ans = 0
for s in input().split():
    if s in ['he', 'she', 'him', 'her']:
        ans+=1
print(ans)