n = int(input())

w = [0] * n
h = [0] * n

for i in range(n):
    a, b = map(int, input().split())
    w[i] = a
    h[i] = b

ma_h = 0
ma_h1 = 0
ma_h_ind = 0
ma_h1_ind = 0

for i in range(n):
    if h[i] >= ma_h:
        ma_h = h[i]
        ma_h_ind = i

for i in range(n):
    if h[i] >= ma_h1 and i != ma_h_ind:
        ma_h1 = h[i]
        ma_h1_ind = i


w_sum = sum(w)

for i in range(n):
    if ma_h_ind == i:
        print((w_sum - w[i])*ma_h1, end=' ')
    else:
        print((w_sum - w[i])*ma_h, end=' ')
