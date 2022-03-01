import sys

s = sys.stdin.readline().rstrip()
dict = []

for idx in range(len(s)):
    dict.append(s[idx:])
dict.sort()
print(*(dict), sep = '\n')