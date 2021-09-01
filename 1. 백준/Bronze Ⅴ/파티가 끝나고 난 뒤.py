L, P = map(int, input().split())
a, b, c, d, e = map(int, input().split())

list = [a, b, c, d, e]

right_answer = L * P
for i in (list):
    print(i - right_answer, end = ' ')