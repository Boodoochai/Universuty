from collections import deque

n, m = map(int, input().split())

l = [list(input()) for i in range(n)]

used = set()
que = deque()

used_squares = set()
used_squares.add((1, 1))
que.append((1, 1))

while que:
    x = que.popleft()
    new_tup = (x[0], x[1])
    if l[x[0] - 1][x[1]] == '.':
        i = 1
        while l[x[0] - i][x[1]] == '.':
            used_squares.add((x[0] - i, x[1]))
            i += 1
        i -= 1
        if (x[0] - i, x[1]) not in used:
            que.append((x[0] - i, x[1]))
            used.add((x[0] - i, x[1]))

    if l[x[0] + 1][x[1]] == '.':
        i = 1
        while l[x[0] + i][x[1]] == '.':
            used_squares.add((x[0] + i, x[1]))
            i += 1
        i -= 1
        if (x[0] + i, x[1]) not in used:
            que.append((x[0] + i, x[1]))
            used.add((x[0] + i, x[1]))

    if l[x[0]][x[1] - 1] == '.':
        i = 1
        while l[x[0]][x[1] - i] == '.':
            used_squares.add((x[0], x[1] - i))
            i += 1
        i -= 1
        if (x[0], x[1] - i) not in used:
            que.append((x[0], x[1] - i))
            used.add((x[0], x[1] - i))

    if l[x[0]][x[1] + 1] == '.':
        i = 1
        while l[x[0]][x[1] + i] == '.':
            used_squares.add((x[0], x[1] + i))
            i += 1
        i -= 1
        if (x[0], x[1] + i) not in used:
            que.append((x[0], x[1] + i))
            used.add((x[0], x[1] + i))

print(len(used_squares))