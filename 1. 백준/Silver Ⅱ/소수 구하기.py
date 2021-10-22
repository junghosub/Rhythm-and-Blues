# 에라토스테네스의 체
import sys

m, n = map(int, sys.stdin.readline().split()) # m 이상, n 이하 입력 받음
prime = [True] * (n+1) # n만큼의 True 리스트 생성
prime[0], prime[1] = False, False

for idx in range(2, int(n**0.5)+1):  # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    if prime[idx] == True: # 만약 해당 인덱스에 위치한 값이 '소수'라면
        for i in range(idx+idx, n+1, idx): # '소수'의 배수를 제외
            prime[i] = False

for i in range(m, n+1):
    if prime[i]:
        print(i)

print(i for i in range(m, n+1) if prime)

for i in range(m, n+1):
    if prime[i] == True and i > 1:
        print(i)

# time : 268ms

# 정수 i까지의 소수를 구하기 위해 제곱근까지 검토하기.
import sys

m, n = map(int, sys.stdin.readline().split()) # m 이상, n 이하 입력 받음

for i in range(m, n+1): # m부터 n까지 확인
    prime = True # 소수라고 가정하기 위해 prime = True
    for j in range(2, int(i**0.5)+1): #
        if i % j == 0:
            prime = False
            break
    if i > 1 and prime:
        print(i)
# time : 1120ms