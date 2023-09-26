def bigger(x):
    l = -1
    r = len(prices)
    while r - l > 1:
        m = (r + l) // 2
        if prices[m] >= x and m not in used:
            l = m
        else:
            r = m
    return l


n, m = map(int, input().split())

prices: list = sorted(list(map(int, input().split())), reverse=True)

su = sum(prices)

l = list(map(int, input().split()))
d = list(map(int, input().split()))

coupons = [(l[i], d[i]) for i in range(m)]

coupons.sort(key=lambda x: x[1], reverse=True)

disc = 0

used = set()

for i in range(m):
    x = bigger(coupons[i][0])
    if x == -1:
        continue
    disc += coupons[i][1]
    used.add(x)

print(su - disc)
