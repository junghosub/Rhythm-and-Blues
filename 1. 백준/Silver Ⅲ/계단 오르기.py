n = int(input())
array = [0]
for _ in range(n):
    array.append(int(input()))

def solve(n):
    if n == 1:
        return array[1]

    else:
        dp = [0] * (n+1)
        dp[1] = array[1]
        dp[2] = dp[1] + array[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + array[i], dp[i-3] + array[i-1] + array[i])

    return dp[n]
print(solve(n))