import sys

n = int(sys.stdin.readline())
company = dict()

for _ in range(n):
    name, log = sys.stdin.readline().split()
    if log == 'enter':
        company[name] = 1
    else:
        del company[name]

for i in sorted(list(company.keys()), reverse=True):
    print(i)