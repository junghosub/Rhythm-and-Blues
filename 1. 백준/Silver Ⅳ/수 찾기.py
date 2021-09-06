n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

def binray_search(a, key):
    pl = 0 # 맨 처음 인덱스
    pr = len(a)-1 # 맨 마지막 인덱스

    while True:
        pc = (pl + pr)//2 # 정중앙의 인덱스
        if a[pc] == key: # pc와 찾고자 하는 값이 같으면 cnt = 1
            return 1
        elif a[pc] < key: # pc가 찾고자 하는 값보다 작다면 검색 범위를 뒤쪽으로
            pl = pc + 1
        else:
            pr = pc -1 # pc가 찾고자 하는 값보다 크다면 검색 범위를 앞쪽으로
        if pl > pr:
            break
    return 0

for i in b:
    print(binray_search(a, i))
