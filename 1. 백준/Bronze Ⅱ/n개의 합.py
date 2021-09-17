a = list(map(int, input().split()))
n = int(input())
sum = 0

def solve(a: list) -> int:
    for i in range(n):
        sum+= a[i]
    return sum

solve(a)