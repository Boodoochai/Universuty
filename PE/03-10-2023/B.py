def rotate(l, x):
    i = x
    j = x
    cur = l[i][j]
    for o in range(x + 1, len(l) - x):
        tmp = cur
        cur = l[x][o]
        l[x][o] = tmp
    for o in range(x + 1, len(l) - x):
        tmp = cur
        cur = l[o][len(l) - x - 1]
        l[o][len(l) - x - 1] = tmp
    for o in range(x + 1, len(l) - x):
        tmp = cur
        cur = l[len(l) - x - 1][len(l) - o - 1]
        l[len(l) - x - 1][len(l) - o - 1] = tmp
    for o in range(x + 1, len(l) - x):
        tmp = cur
        cur = l[len(l) - o - 1][x]
        l[len(l) - o - 1][x] = tmp


n = int(input())
l = [list(input()) for i in range(n)]

# for i in range(n//2 - 1 + n%2):
#    rotate(l, i)
rotate(l, 0)

for i in range(n):
    print(*l[i], sep='')
