import sys

n = int(sys.stdin.readline())
books = dict()

for _ in range(n):
    book = sys.stdin.readline().rstrip()
    books.setdefault(book, 0)
    books[book] += 1
print(sorted(list(books.items()), key = lambda x: (-x[1], x[0]))[0][0])