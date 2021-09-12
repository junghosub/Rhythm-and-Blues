import sys

result = 0 # 캠핑장 최대 사용일수
i  = 1 # iterantion

while True:
    l,p,v = list(map(int, sys.stdin.readline().split())) # p일 중, l일 사용 가능하다. v일짜리 휴가
    if l+p+v == 0: # 만약 l,p,v가 0이면 종료
        break
    result = (v // p) * l # p일 중 l일 최대 사용
    result += min(v % p, l) # 나머지 더해줌
    print('Case {0}: {1}'.format(i, result))
    i+=1