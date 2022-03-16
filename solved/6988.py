n = int(input())
tiles = [int(x) for x in input().split()]
tile_idx = {tile: i for i, tile in enumerate(tiles)}

tiles_by_interval = {}
for i in range(n):
    for j in range(i+1, n):
        interval = tiles[j]-tiles[i]
        if tiles[j]+interval in tile_idx:
            if interval not in tiles_by_interval:
                tiles_by_interval[interval] = []
            tiles_by_interval[interval].append(tiles[i])

# dp[interval][last_tile] = 그 타일까지 최대값
# dp[interval][i+interval] = dp[interval][i]+i+interval (직전 인터벌의 타일 있으면)
ans = 0
dp = {interval: {} for interval in tiles_by_interval}
for itv in tiles_by_interval:
    for i in range(n):
        tile = tiles[i]
        if tile not in dp[itv] and tile-itv in tile_idx and tile-itv*2 in tile_idx:
            dp[itv][tile] = tile*3-itv*3
        if tile in dp[itv] and tile+itv in tile_idx:
            dp[itv][tile+itv] = dp[itv][tile]+tile+itv
        if tile in dp[itv]:
            ans = max(ans, dp[itv][tile])
# print(dp)
print(ans)
