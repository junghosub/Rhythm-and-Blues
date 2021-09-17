A, B = list(map(str, input().split()))

A = [A[2-i] for i in range(3)]
B = [B[2-j] for j in range(3)]

print(*(A if A>B else B), sep = '')
