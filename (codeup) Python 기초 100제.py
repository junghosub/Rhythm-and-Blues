# 6001
print('Hello')

# 6002
print('Hello World')

# 6003
print('Hello')
print('World')

# 6004
print('Hello')

# 6005
print('"Hello World')

# 6006
print('"!@#$%^&*()\"')

# 6007
print('"C:\\Download\\\'hello\.py')

# 6008
print('print(\"Hello\\nwolrd\")')

# 6009
c = input()
print(c)

# 6010
n = input()
n = int(n)
print(n)

# 6011
f = input()
f = float(f)
print(f)

# 6012
a = input()
b = input()
print(a)
print(b)

# 6013
a = input()
b = input()
print(b)
print(a)

# 6014
f = input()
f = float(f)
print(f)
print(f)
print(f)

# 6015
a, b = input().split()
print(a)
print(b)
# tip : input().split()을 사용하면, 공백을 기준으로 입력된 값들을 나누어 자른다. 하지만 다른 프로그래밍 언어에서는 적용되지 않음.

# 6017
s = input()
print(s,s,s,)

# 6018
a, b = input().split(':')
print(a, b, sep = ':')
# tip : input().split(':')을 사용하면 ': 기호를 기준으로 나눈다. print(sep = ':')을 사용하면 ':' 기호를 사이에 두고 값을 출력한다.

# 6019
y, m, d= input().split('.')
print(d,m,y, sep = '-')

# 6020
a, b = input().split('-')
print(a, b, sep = '')

# 6021
a =  input()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

# 6022
y = input()
print(y[:2], y[2:4], y[4:6])

# 6023
h, m, s = input().split(':')
print(m)

# 6024
a, b = input().split()
s = a + b
print(s)

# 6025
a, b = input().split()
s = int(a) + int(b)
print(s)

# 6026
a = input()
b = input()
s = float(a) + float(b)
print(s)

# 6027
a = input()
n = int(a)
print('%x' % n)
# tip : %x는 16진수(hexadeciaml)을 의미한다.

# 6028
a = input()
n = int(a)
print('%X' % n)

# 6029
a = input()
n = int(a, 16)
print('%o' % n)

# 6030
n = ord(input())
print(n)
# tip : ord(input())은 입력 받은 문자를 10진수 유니코드 값을 변환 후, n에 저장한다. ord(Ordinal Postion)은 어떤 문자의 순서 위치를 의미한다.

# 6031
c = int(input())
print(chr(c))

# 6032
c = int(input())
print(-c)

# 6033
c = ord(input())
print(chr(c+1))

# 6034
a, b = input().split()
c = int(a) - int(b)
print(c)

# 6035
a, b = input().split()
c = float(a) * float(b)
print(c)

# 6036
w, r = input().split()
print(w * int(r))

# 6037
r = input()
w = input()
print(w * int(r))

# 6038
a, b = input().split()
print(pow(int(a), int(b)))

# 6039
f1, f2 = input().split()
print(pow(float(f1), float(f2)))

# 6040
a, b = input().split()
c = int(a) / int(b)
print(c)

# 6041
a, b = input().split()
c = int(a) % int(b)
print(int(c))

# 6042
a = input()
print(round(float(a), 2))

# 6043
f1, f2 = input().split()
c = float(f1) / float(f2)
print(round(c, 3))

# 6044
a, b = input().split()
print(int(a) + int(b))
print(int(a) - int(b))
print(int(a) * int(b))
print(int(int(a) / int(b)))
print(int(a) % int(b))
print(round(int(a) / int(b),2))

# 6045 정수 3개를 입력 받아 합과 평균 출력하기
a, b, c = input().split()
sum = int(a) + int(b) + int(c)
average = sum / 3
print(sum, round(average, 3))

# 6046 정수 1개를 입력 받아 2배곱 출력
a = input()
b = int(a) * 2
print(b)

# 6047 2의 거듭제곱 배로 곱해 출력
a, b = input().split()
c = int(a) * pow(2, int(b))
print(c)

# 6048 정수 2개를 입력 받아 비교
a, b = input().split()
if int(a) < int(b):
    print(True)
else:
    print(False)

a, b = input().split()
print(a < b)
# tip: 위의 예시처럼 비교 연산자를 사용하는 것이 더욱 간편하다.

# 6049 정수 2개를 입력 받아 비교2
a, b = input().split()
print(a == b)

# 6050 정수 2개를 입력 받아 비교3
a, b = input().split()
print(float(a) <= float(b))

# 6051 정수 2개를 입력 받아 비교4
a, b = input().split()
print(float(a) != float(b))

# 6052 정수 입력 받아 참 거짓 평가
a = int(input())
print(a != 0)

# 6053 참거짓 바꾸기
a = int(input())
print(not bool(a))
# 또 다른 예시
a = bool(int(input()))
print(not a)

# 6054 둘 다 참일 경우에 출력
a, b = input().split()
print(bool(int(a)) & bool(int(b)))

# 6055 하나라도 참이면 참 출력
a, b = input().split()
print(bool(int(a)) | bool(int(b)))

# 6056 참/거짓이 다른 경우에 참 출력
a, b = input().split()
print(bool(int(a)) ^ bool(int(b)))

# 6057 참/거짓이 서로 같을 때 참 출력하기
a, b = input().split()
print(bool(int(a)) == bool(int(b)))

# 6058 둘 다 거짓일 경우 참 출력하기
a, b = input().split()
print((not bool(int(a))) & (not bool(int(b))))

# 6059 비트 단위로 NOT 하여 출력하기
a = int(input())
b = ~a
print(b)
# tip : 참/거짓으로 바꾸려면 비트 단위 연산자인 ~를 붙이면 된다. (~, tilde, 틸드라고 읽는다.)

# 6060 비트 단위로 AND 하여 출력하기
a, b = input().split()
print(int(a) & int(b))
# tip : AND 연산하려면 비트 단위 연산자인 &를 사용하면 된다. (and, ampersand, 엠퍼센드라고 읽는다.)

# 6061 비트 단위로 OR하여 출력하기
a, b = input().split()
print(int(a) | int(b))
# tip : OR 연산하려면 비트 연산자인 |를 사용하면 된다. (or, vertical bar, 버티컬바라고 읽는다.)
# pipe 연산자라고도 읽는다.

# 6062 비트 단위로 XOR하여 출력
a, b = input().split()
print(int(a) ^ int(b))

# 6063 정수 2개를 입력 받아 큰 값 제출하기
a, b = input().split()
if int(a) >= int(b):
    max = int(a)
else:
    max = int(b)

print(int(max))

# c = (int(a) if (a>=b) else int(b))
# print(int(c)) 이 방법이 더 효율적이다.

# 6064 정수 3개를 입력받아 가장 작은 값 출력하기
a, b, c = input().split()
d = (int(a) if (int(a) <= int(b)) else int(b))
e = (int(d) if (int(d) <= int(c)) else int(c))
print(int(e))

# 6065 정수 3개를 입력받아 짝수만 출력하기
a, b, c = input().split()
list = [int(a), int(b), int(c)]

for i in list:
    if i % 2 == 0:
        print(i)

# 6066 정수 3개를 입력 받아 짝/홀 출력하기
a, b, c = input().split()
list = [int(a), int(b), int(c)]

for i in list:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')

# 6067 숫자 분류하기
a = int(input())

if (a < 0) & (a % 2 == 0):
    print('A')
elif (a < 0) & (a % 2 != 0):
    print('B')
elif (a > 0) & (a % 2 == 0):
    print('C')
else:
    print('D')

# 6068 점수 입력 받아 평가하기
a = int(input())

if a >= 90:
    print('A')
elif a >= 70:
    print('B')
elif a >= 40:
    print('C')
else:
    print('D')

# 6069 평가 입력 받아 다르게 출력하기
word = str(input())

if word == 'A':
    print('best!!!')
elif word == 'B':
    print('good!!')
elif word == 'C':
    print('run!')
elif word == 'D':
    print('slowly~')
else:
    print('what?')

# 6067 월 입력받아 계절 출력하기
month = int(input())

if month // 3 == 1:
    print('spring')
elif month // 3 == 2:
    print('summer')
elif (month // 3 == 3):
    print('fall')
else:
    print('winter')

# 수의 특징을 관찰하고, 이용하면 간단히 해결할 수 있다,

# 6071 0이 입력할 때까지 무한출력
n = 1 # 처음 조건을 통과하기 위해 0이 아닌 값 임의 저장
while n!=0: # 조건식이 false가 되면 반복문 종료
    n = int(input())
    if n!=0:
        print(n)

# 6072 카운트 다운
a = int(input())

for i in range(a):
    print((int(i) - a) * -1)

# 6073 카운트다운
a = int(input())

for i in range(a):
    print((int(a) - int(i) -1))

# 6074 알파벳 출력하기
c = ord(input())
t = ord('a')
while t <= c:
    print(chr(t), end = ' ')
    t += 1

# 알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
# chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있다.
# print(.. end =' ')와 같이 작성하면 값 출력 후, 공백 문자 ' '를 출력한다.

# 6075 원하는 숫자까지 출력하기
a = int(input())

for i in range(a+1):
    print(i)

# range(끝), range(시작, 끝), range(시작, 끝, 증감) 형태로 표현 가능하다.

# 6077 짝수의 합 구하기
a = int(input())
even = 0

for i in range(a + 1):
    if i % 2 == 0:
        even += i
print(even)

# 6078 pass!

# 6079 언제까지 더해야 할까?
a = int(input())
sum = 0

for i in range(a):
    sum += i
    if sum >= a:
        print(int(i))
        break

# 6080 주사위 2개 던지기
n, m = input().split()

for i in range(int(n)):
    for j in range(int(m)):
        print(i + 1, j + 1)


# 6081 16진수 구구단 출력

# 6082 3,6,9의 왕이 되자
a = int(input())

for i in range(1, a + 1):
    if (i % 10 == 3) or (i % 10 == 6) or (i % 10 == 9):
        print('X', end = ' ')
    else:
        print(i, end = ' ')

# 틀렸었음. 수의 패턴을 파악하는 것이 중요하다!

# 6083 rgb를 섞어 색 만들기
r, g, b = map(int, input().split())

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k, end = ' ')
            print()
print(r * g * b)

# 6084 소리 파일 저장용량 계산하기
# 1초 동안 마이크로 소리 강약을 체크하는 횟수 : h
# 한번 체크한 값을 저장할 때 사용하는 비트 수 : b
# 좌우 등 소리를 저장할 트랙 개수인 채널 개수 : c
# 녹음할 시간 : s
h, b, c, s = map(int, input().split())

mb = h * b * c * s / 8/ 1024 / 1024
print(round(mb, 1), 'MB')

# 6085 그림 파일 저장용량 계산하기
# 가로 해상도 : w
# 세로 해상도 : h
# 한 픽셀을 저장하기 위한 비트 : b
w, h, b = map(int, input().split())
mb = w * h * b / 8 / 1024 / 1024
print(round(mb, 2), 'MB')

# 6086 거기까지! 이제 그만
n = int(input())
sum = 0
for i in range(n + 1):
    sum += i
    if sum >= n:
        print(sum)
        break

# 6087 3의 배수는 통과!
n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        print('', end = '')
    else:
        print(i, end = ' ')

# 6088 등차수열의 수 나열하기
a, d, n = map(int, input().split())

list = []
for i in range(100):
    answer = a + (i * d)
    list.append(answer)
print(list[n - 1])

# 6089 등비수열의 수 나열하기
a, r, n = map(int, input().split())
list = []

for i in range(0, 11):
    if i == 0:
        answer = a * pow(r, (i))
        list.append(answer)
    else:
        answer = a * pow(r, (i-1))
        list.append(answer)

print(list[n])

# 6090 수 나열하기3
a, m, d, n = map(int, input().split())
list = []

for i in range(0,11):
    if i == 0:
        answer = a
        list.append(answer)
    else:
        answer = answer * m + d
        list.append(answer)
print(list[n-1])

# 6091 함께 푸는 날
import math
a, b, c = map(int, input().split())

def lcm(a, b, c):
    gcd1 = a * b // math.gcd(a,b)
    gcd2 = gcd1 * c // math.gcd(gcd1, c)
    return gcd2

print(lcm(a,b,c))

# 6092 이상한 출석 번호 부르기
from collections import Counter
n = int(input())
data = list(map(int, input().split()))
count = Counter(data)

for i in count:
    print(count[i])

# 6093 이상한 출석 번호 부르기2
n = int(input())
data = list(map(int, input().split()))

for i in range(1,n + 1):
    print(data[-i], end = ' ')

# 6094 이상한 출석 번호 부르기3
n = int(input())
data = list(map(int, input().split()))
data.sort()
print(data[0])

# 6095 바둑판에 흰 돌 올려놓기
n = int(input())
matrix = []

for i in range(n):
    xy = list(map(int, input().split()))
    matrix.append(xy)

for i in range(1,20):
    print()
    for j in range(1, 20):
        if [i,j] in matrix:
            print('1', end = ' ')
        else:
            print('0', end = ' ')

# 위와 같은 방법도 있지만 아래와 같이 list comprehension을 사용하여 짧게 만들 수 있다.
d = [[0 for j in range(20)] for i in range(20)]
