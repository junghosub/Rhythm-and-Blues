# 정수 입력
n = int(input()) # 26
num = n
count = 0 # 사이클의 개수

while True:
    a = num // 10 # '2'6 십의 자리
    b = num % 10 # 2'6' 일의 자리
    c = (a + b) % 10 # 8 십의 자리 수와 일의 자리 수를 더함
    num = (b * 10)+ c # 68 일의 자리 * 10과 (십의 자리 + 일의 자리)를 더해줌.

    count += 1
    if (num == n):
        break
print(count)