n = int(input())
road = [int(x) for x in input().split()]
price = [int(x) for x in input().split()]

sum_price = 0
min_price = price[0]
for i in range(1, n):
    if price[i-1] < min_price:
        min_price = price[i-1]
    sum_price += min_price*road[i-1]
    # print(sum_price)

print(sum_price)
