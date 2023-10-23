n = int(input())

dp = [999999999999999999999999999] * (n+1)

dp[0] = 0
dp[1] = 1
for i in range(2, n+1):
    j = 1
    while j**3 <= i:
        dp[i] = min(dp[i], dp[i-j**3] + 1)
        j += 1

print(dp[n])
