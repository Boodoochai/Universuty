n = int(input())
l = sorted(list(map(int, input().split())))

for i in range(n):
    q = l[i]
    fl = 0
    fll = 0
    for j in range(n):
        if l[j] % q != 0:
            fl = 1
            break
    if fl == 0:
        fll = 1
        print(q)
        break
if fll == 0:
    print(-1)