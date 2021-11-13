t = int(input())
stack = []

for _ in range(t):
    sentence = input()
    sentence = sentence[::-1].split()

    print(*(sentence[::-1]))

t = int(input())

for _ in range(t):
    sentence = input()[::-1]
    print(sentence.split()[::-1])