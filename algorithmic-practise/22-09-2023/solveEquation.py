import math


def isEnough(m):
    if m*m + m**(1/2) <= c:
        return True
    return False


c = int(input())

l = 0
r = 10**18

for i in range(10**6):
    m = (r+l) / 2
    if isEnough(m):
        l = m
    else:
        r = m

print(l)