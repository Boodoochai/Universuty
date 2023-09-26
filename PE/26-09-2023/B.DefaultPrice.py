n, m = map(int, input().split())

plates_colors = list(input().split())

colors = list(input().split())
colors_prices = list(map(int, input().split()))

price = 0

for x in plates_colors:
    if x not in colors:
        price += colors_prices[0]
    else:
        price += colors_prices[colors.index(x)+1]

print(price)
