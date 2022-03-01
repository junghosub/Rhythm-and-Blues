import sys

n = int(sys.stdin.readline())
tickets = list(map(int, sys.stdin.readline().split()))

x = 1
for ticket in tickets:
    if ticket == x:
        x += 1
    else:
        print(x)
        sys.exit(0) # 프로그램을 정상적으로 종료시키고 싶을 때 사용
print(tickets[-1] + 1)
