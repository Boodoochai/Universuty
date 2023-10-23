n = int(input())

s = set()
k = 0
for i in range(n):
    a = input()
    if a not in s and a == a[::-1]:
        k += 1
    s.add(a)
    s.add(a[::-1])

print((k+len(s))//2)