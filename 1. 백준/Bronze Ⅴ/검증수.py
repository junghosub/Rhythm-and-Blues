A, B, C, D, E = map(int, input().split())
list = [A, B, C, D, E]

sum = 0
for i in (list):
    sum += pow(i, 2)

print(sum % 10)

