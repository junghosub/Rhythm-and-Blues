# 아이디어 : 반을 버려야 되니까 가장 양이 적은 음료수를 버리고, 가장 양이 많은 음료수에 추가한다.

n = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

for idx in range(n-1):
    drinks[-1] += drinks[idx]/2
print(drinks[-1])