def find_smaller(x):
    l = -1
    r = len(bomb)

    while r - l > 1:
        m = (r + l) // 2
        if bomb[m] <= x:
            l = m
        else:
            r = m
    return l


n = int(input())
sel = list(map(int, input().split()))
m = int(input())
bomb = list(map(int, input().split()))
bomb_uns = {bomb[i] : i for i in range(len(bomb))}
bomb.sort()

for x in sel:
    q1 = find_smaller(x)
    q1 = max(q1, 0)
    q1 = min(q1, len(bomb)-2)
    if abs(bomb[q1] - x) < abs(bomb[q1+1] - x):
        print(bomb_uns[bomb[q1]]+1, end=' ')
    else:
        print(bomb_uns[bomb[q1+1]]+1, end=' ')