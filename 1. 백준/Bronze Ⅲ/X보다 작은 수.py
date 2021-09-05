N, X = map(int, input().split())
A = list(map(int,input().split()))

# 숏코딩으로 해봄
print(*(i for i in A if i < X))
