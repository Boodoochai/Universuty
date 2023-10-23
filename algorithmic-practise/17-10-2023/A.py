n = int(input())

l = list(map(int, input().split()))

if n == 1:
    print(l[0])
    exit()

dp = [0] * n
dp[0] = l[0]
dp[1] = l[1]

for i in range(2, n):
    dp[i] = l[i] + min(dp[i-1], dp[i-2])

print(dp[n-1])
