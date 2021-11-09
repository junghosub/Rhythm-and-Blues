import sys

n, b = map(int,sys.stdin.readline().split())
notation = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = []

while n >= 1:
    answer.append(notation[n % b])
    n //= b
print(*(reversed(answer)), sep ='')