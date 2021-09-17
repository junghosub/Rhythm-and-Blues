# 봉우리의 수, 활잡이의 수
N = int(input())
mountain = list(map(int, input().split()))
lst = []

for i in range(N):
    archer = mountain[i]
    count = 0
    for j in range(i,N):
        if archer > mountain[j]:
            count += 1
    lst.append(count)
print(max(lst))

# 구글링 결과
num=int(input())
hills=[int(x) for x in input().split()]

res=0
highest=0
cnt=0

for hill in hills :
    if hill > highest :
        highest = hill
        cnt = 0
    else :
        cnt +=1
    res = max(res, cnt)

print(res)