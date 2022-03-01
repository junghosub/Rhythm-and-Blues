def solve(n):
    if n <= 2:
        return dp0[n], dp1[n]
    else:
        for i in range(3, n+1):
            dp0[i] = dp0[i-1] + dp0[i-2]
            dp1[i] = dp1[i-1] + dp1[i-2]
        return dp0[n], dp1[n]

t = int(input())
for _ in range(t):
    n = int(input())
    dp0 = [0] * (40+1)
    dp1 = [0] * (40+1)

    dp0[0], dp0[1], dp0[2] = 1, 0, 1
    dp1[0], dp1[1], dp1[2] = 0, 1, 1
    print(*(solve(n)))