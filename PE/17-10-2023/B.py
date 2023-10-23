n, d = map(int, input().split())

l = [list(input()) for i in range(n)]

k = 0
ma = 0
for i in range(d):
    fl = 0
    for j in range(n):
        if l[j][i] == 'x':
            fl = 1
            ma = max(ma, k)
            k = 0
    if fl == 0:
        k += 1

ma = max(ma, k)

print(ma)
