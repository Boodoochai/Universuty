n = int(input())

dp = [[0] * (100) for i in range(n+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(100):
        for k in range(10):
            if j >= k:
                dp[i][j] += dp[i-1][j-k]

ans = 0
for i in range(100):
    ans += dp[n][i]**2

print(ans)