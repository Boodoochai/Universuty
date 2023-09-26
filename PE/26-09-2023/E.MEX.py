n = int(input())
l = list(map(int, input().split()))
s = list(input())

m = [0] * 3
x = [0] * 3

for i in range(n):
    if s[i] == 'X':
        x[l[i]] += 1

ans = 0

for i in range(n):
    if s[i] == 'M':
        m[l[i]] += 1
    if s[i] == 'X':
        x[l[i]] -= 1
    if s[i] == 'E':
        for j in range(3):
            for k in range(3):
                t = set()
                t.add(0)
                t.add(1)
                t.add(2)
                t.add(3)
                if j in t:
                    t.remove(j)
                if k in t:
                    t.remove(k)
                if l[i] in t:
                    t.remove(l[i])
                ans += min(t) * m[j] * x[k]

print(ans)
