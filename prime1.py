# 1,000 이하인 소수를 나열하기

counter = 0 # 나눗셈 횟수를 카운트

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0:
            break
    else:
        print(n)
print(f'나눗셈을 실행한 횟수 : {counter}')

# 알고리즘 개선하기1
counter = 0 # 나눗셈 횟수를 카운트
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2): # 홀수만을 대상으로 설정
    for i in range(1, ptr):
        counter += 1
        if n% prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수 : {counter}')

# 알고리즘 개선하기2
counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        # counter가 2회 증가하는 이유는 곱셈 (prime[i] * prime[i]와 나눗셈 (n % prime[i]). 두 연산이 실행되기 때문이다.
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수 : {counter}')