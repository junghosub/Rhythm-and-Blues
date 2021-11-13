import sys
s = sys.stdin.readline().rstrip()
lower = [chr(i) for i in range(97,123)]
upper = [chr(i) for i in range(65,91)]
password = []

for alphabet in s:
    if alphabet in lower:
        password.append(lower[(lower.index(alphabet)+13)%26])
    elif alphabet in upper:
        password.append(upper[(upper.index(alphabet)+13)%26])
    else:
        password.append(alphabet)
print(*(password), sep = '')