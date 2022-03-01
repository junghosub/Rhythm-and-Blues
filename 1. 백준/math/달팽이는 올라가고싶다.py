import sys

a, b, v = map(int, sys.stdin.readline().split())
print((v-b-1) //(a-b)+1)