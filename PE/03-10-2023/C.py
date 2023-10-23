n, k = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

l.sort()

su = 0
for i in range(n):
    su += l[i][1]

if su <= k:
    print(1)
    exit(0)

i = 0
while su > k:
    su -= l[i][1]
    i += 1

print(l[i - 1][0] + 1)
