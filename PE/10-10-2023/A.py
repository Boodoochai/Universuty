n, p, q = map(int, input().split())

l = list(map(int, input().split()))

v1 = p

v2 = q+min(l)

print(min(v1, v2))