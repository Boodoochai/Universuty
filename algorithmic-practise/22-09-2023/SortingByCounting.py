n = int(input())
l = list(map(int, input().split()))

a = [0 for i in range(10**6+1)]

for x in l:
    a[x] += 1

ans = []

for i in range(len(a)):
    while a[i] > 0:
        a[i] -= 1
        ans.append(i)

print(*ans)