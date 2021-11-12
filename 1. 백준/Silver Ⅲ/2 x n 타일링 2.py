import sys

def dp(n):
    dp = [0 for _ in range(1001)] # 메모이제이션을 위한 리스트 생성
    dp[1], dp[2] = 1,3 # 초기값 설정
    for i in range(3, n+1):
        dp[i] = dp[i-1]+ (2*dp[i-2]) # 점화식
    return dp[n]
print(dp(int(sys.stdin.readline())) % 10007)