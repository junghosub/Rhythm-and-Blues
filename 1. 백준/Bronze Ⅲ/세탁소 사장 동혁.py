T = int(input())

array = [25, 10, 5, 1]

def solve(C, array):
    for i in array:
        count = 0
        count += C // i
        C %= i
        print(count, end = ' ')

for _ in range(T):
    C = int(input())
    solve(C, array)