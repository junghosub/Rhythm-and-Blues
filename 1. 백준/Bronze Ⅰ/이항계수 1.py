import math

n, k = map(int, input().split())

def nCr(n,r): # n : 전체 개수, r : 뽑을 개수
    cnt = math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
    return cnt

print(nCr(n,k))
