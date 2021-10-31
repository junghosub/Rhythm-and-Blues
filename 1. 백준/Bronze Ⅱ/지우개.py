import sys

n = int(sys.stdin.readline())
string = [i for i in range(1, n+1)]

while len(string) != 1:
    for i in range(len(string)):
        if (i+1) % 2 != 0:
            string[i] = ''
    string = [i for i in string if i]
print(string[-1])