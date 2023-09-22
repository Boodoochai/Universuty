n = int(input())

l = set(map(int, input().split()))

s = {i for i in range(1, n+1)}

ans = s - l

print(len(ans))
print(*sorted(ans))
