import functools


def compare(x, y):
    if (x[0]*(y[0]+y[1])) > (y[0]*(x[0]+x[1])):
        return -1
    elif (x[0]*(y[0]+y[1])) < (y[0]*(x[0]+x[1])):
        return 1
    else:
        return 0

n = int(input())

a = list()
b = list()

for i in range(n):
    q, w = map(int, input().split())
    a.append(q)
    b.append(w)

success_rate = [(a[i], b[i], i) for i in range(n)]

success_rate.sort(key=functools.cmp_to_key(compare))

for i in range(n):
    print(success_rate[i][2]+1)
