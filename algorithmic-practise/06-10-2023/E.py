n = int(input())
l = list(map(int, input().split()))

d = dict()

k = [2**i for i in range(60)]

ans = 0

for i in range(n):
    for j in range(len(k)):
        if (k[j] - l[i]) in d.keys():
            ans += d[k[j] - l[i]]
    if l[i] in d.keys():
        d[l[i]] += 1
    else:
        d[l[i]] = 1

print(ans)
