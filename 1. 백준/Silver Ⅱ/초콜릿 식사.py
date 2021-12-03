import sys

k = int(sys.stdin.readline())

chocolate, cnt = 0,0
i = 0

while k > 2**i:
    i += 1
chocolate = 2**i

answer = chocolate

while k > 0:
    if chocolate > k:
        chocolate //= 2
        cnt += 1
    else:
        k -= chocolate
print(answer, cnt)