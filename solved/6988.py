n = int(input())
tiles = [int(x) for x in input().split()]
tile_idx = {tile: i for i, tile in enumerate(tiles)}

ans = 0
dp = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        diff = tiles[j]-tiles[i]
        if tiles[i]-diff in tile_idx:
            before = tile_idx[tiles[i]-diff]
            if dp[before][i] > 0:
                dp[i][j] = dp[before][i]+tiles[j]
            else:
                dp[i][j] = tiles[i]*3
            ans = max(ans,dp[i][j])
print(ans)