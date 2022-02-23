dp = [0 for _ in range(1000001)]
dp[1] ,dp[2], dp[3] = 1, 2, 4
for i in range(4, 1000000+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])