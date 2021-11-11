import sys

def dp(n):
    dp = [0 for _ in range(1001)]
    dp[1], dp[2] = 1,2
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n] % 10007
print(dp(int(sys.stdin.readline())))