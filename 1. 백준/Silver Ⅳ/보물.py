# 아이디어는 B의 최댓값에 A의 최솟값을 곱해주면 됨.
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res=0

for _ in range(n):
    min_a = min(a)
    max_b = max(b)
    res += min_a * max_b
    a.remove(min_a)
    b.remove((max_b))
print(res)