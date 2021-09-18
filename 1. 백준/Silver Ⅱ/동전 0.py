import sys
n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
cnt = 0

for coin in coins[::-1]:
    if coin <= k:
        cnt += k//coin
        k %= coin
print(cnt)
