from math import *


def all_dels_set(x):
    dels = set()
    for i in range(1, int(sqrt(x) + 1) + 1):
        if x % i == 0:
            dels.add(i)
            dels.add(x // i)
    return dels


n, m = map(int, input().split())

dels_n = all_dels_set(n)
dels_m = all_dels_set(m)

print(*sorted(dels_n & dels_m), sep='\n')
