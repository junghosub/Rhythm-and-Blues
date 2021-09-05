t = int(input())
lst = []

for _ in range(t):
    a, b = map(int, input().split())
    lst.append(a + b)

for i in lst:
    print(i)

# 처음 생각했던 아래 방법과 같이 해도 된다고 한다.
# for _in range(t):
    # a, b = map(int, input().split()
    # print (a + b)