n, d = map(int, input().split())

friends = [list(map(int, input().split())) for i in range(n)]

friends.sort()

l = 0
r = 0
su = friends[0][1]
ans = su

while r < n-1:
    r += 1
    su += friends[r][1]
    if friends[r][0] - friends[l][0] < d:
        ans = max(ans, su)
    else:
        while friends[r][0] - friends[l][0] >= d:
            su -= friends[l][1]
            l += 1
    if friends[r][0] - friends[l][0] < d:
        ans = max(ans, su)

print(ans)