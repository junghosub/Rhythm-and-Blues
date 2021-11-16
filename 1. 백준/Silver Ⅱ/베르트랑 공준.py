import sys

def eratosthenes(n):
    prime = [True for _ in range(2*n+1)]
    prime[0], prime[1] = False, False

    for i in range(n, 2*n+1):
        if prime[i] == True:
            for j in range(2, int(i**0.5)+1):
                if i == 2:
                    continue
                elif i % j == 0:
                    prime[i] = False
                    for k in range(j+j, 2*n+1, j):
                        prime[k] = False

    answer = [int(i) for i in range(n+1, 2*n+1) if prime[i]]
    return len(answer)

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(eratosthenes(n))