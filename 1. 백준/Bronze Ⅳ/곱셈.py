# 문자열을 사용하여 출력함.
A = int(input())
B = str(input())

for i in range(0, 3):
    print(A * int(B[2 - i]))
print(A * int(B))