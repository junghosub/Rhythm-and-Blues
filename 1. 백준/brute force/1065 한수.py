# 1,000보다 작거나 같은 자연수 n에 대해서 한수를 구함
import sys

n = int(sys.stdin.readline()) # 정수 n 입력 받음
cnt = 0 # count
for i in range(1,n+1):
    if i <= 99:
        cnt += 1
    else:
        nums = list(map(int,str(i)))
        if nums[0]-nums[1]==nums[1]-nums[2]:
            cnt+=1
print(cnt)

