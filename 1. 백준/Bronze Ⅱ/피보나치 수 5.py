# 재귀적 풀이
def fibonacci(n):
    return fibonacci(n-1)+fibonacci(n-2) if n >= 2 else n

for n in range(1, 11):
    print(n, fibonacci(n))
# 시간복잡도는 O(2^n)

# 반복적 풀이
def fibonacci(n):
    if n < 2:
        return n
    a,b = 0,1
    for i in range(n-1):
        a,b = b, a+b
    return b

for n in range(1, 11):
    print(n, fibonacci(n))
# 시간복잡도는 O(n)

# dp를 활용한 방법
def fibonacci(n):
    if n < 2:
        return n
    cache = [0 for _ in range(n+1)]
    cache[1] = 1

    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

print(fibonacci(int(input())))
