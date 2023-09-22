def isEnough(m):
    q = 0
    for i in range(k):
        q += s[i] // m
    if q >= n:
        return True
    return False


n, k = map(int, input().split())

s = [int(input()) for i in range(k)]

l = 1
r = n+1

while r - l > 1:
    m = (r+l) // 2
    if isEnough(m):
        l = m
    else:
        r = m

print(l)
q = n
fl = 0
for i in range(k):
    if fl == 1:
        break
    while s[i] >= l:
        s[i] -= l
        print(i+1)
        q -= 1
        if q == 0:
            fl = 1
            break