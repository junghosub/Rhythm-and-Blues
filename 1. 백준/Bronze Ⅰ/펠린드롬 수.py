while True:
    n = str(input())
    if n == '0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')

while True:
    n = str(input())
    if n == '0':
        break
    print('yes' if n == n[::-1] else 'no')