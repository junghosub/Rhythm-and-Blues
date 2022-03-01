import sys

def dp(n):
    dp = [0]*11 # 메모이제이션을 위해 배열 생성
    dp[1], dp[2], dp[3] = 1,2,4 # 초기 항 지정
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] # 일반항(i>3)
    return dp[n]

t = int(sys.stdin.readline())
for _ in range(t):
    print(dp(int(sys.stdin.readline())))