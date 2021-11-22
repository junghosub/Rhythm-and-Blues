n = int(input())
matrix = []
for _ in range(n):
    x, y = map(int, input().split())
    matrix.append([x,y])

for i in sorted(matrix, key = lambda x : (x[1], x[0])):
    print(*i)
