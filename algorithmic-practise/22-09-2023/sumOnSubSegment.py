n = int(input())
l = list(map(int, input().split()))

q = [0] * n

q[0] = l[0]
for i in range(1, n):
    q[i] = l[i] + q[i-1]

k = int(input())

for i in range(k):
    a, b = map(int, input().split())
    print(q[b-1] - q[a-1] + l[a-1])