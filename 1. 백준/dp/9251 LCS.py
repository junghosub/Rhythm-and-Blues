def solve(i,j):
    if s2[i] == s1[j]:
        dp[i][j] = dp[i-1][j-1] + 1
    else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

s1 = [0] + list(map(str, input()))
s2 = [0] + list(map(str, input()))

dp = [[0] * (len(s1)) for _ in range(len(s2))]

for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        solve(i,j)
print(max(map(max, dp)))