# 1. 삼중 for문을 통해
n = int(input())
arr = list(map(int, input().split()))

res = 0
for i in range(n):
    for j in range(n):
        for k in range(i,j):
            s += arr[k]
            if s > res:
                res = s
        s = 0

# 2. 부분 수열의 합을 통해
n = int(input())
arr = list(map(int, input().split()))

# prefix sum 구하기
p = [0]
s = 0
for i in arr:
    s += i
    p.append(s)

s = -1000
res = 0
for i in range(1, n):
    for j in range(i, n):
        s = max(s, p[j] - p[i-1])
print(s)

# 3. Divide and Conquer (연습)

# 4. DP
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])

print(max(dp))