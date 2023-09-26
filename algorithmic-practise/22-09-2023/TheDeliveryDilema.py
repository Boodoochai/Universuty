import sys
input = sys.stdin.readline

def isEnough(a, b, m):
    s = 0
    for i in range(len(a)):
        if a[i] > m:
            s += b[i]
        if s > m:
            return False
    return True


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    l = 0
    r = sum(b)

    while r - l > 1:
        m = (r + l) // 2
        if isEnough(a, b, m):
            r = m
        else:
            l = m
    print(r)


t = int(input())

for i in range(t):
    solve()