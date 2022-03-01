n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))
matrix.sort()

for i in range(len(matrix)):
    print(*(matrix[i]))

# 재구현
n = int(input())
matrix = []
for _ in range(n):
    x, y = map(int, input().split())
    matrix.append([x,y])

for i in sorted(matrix, key = lambda x : (x[0], x[1])):
    print(*i)
