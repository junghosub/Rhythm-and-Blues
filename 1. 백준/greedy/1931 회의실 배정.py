def solution():
    k = 0
    cnt = 0
    # 회의 시작 시간이 이전 회의의 종료 시간보다 크거나 같다면 +1
    for time in schedule:
        if time[0] >= k:
            k = time[1]
            cnt += 1
    return cnt

n = int(input())
schedule = []

for _ in range(n):
    s, f = map(int, input().split())
    schedule.append([s,f])

# 회의 종료 시간 -> 회의 시작 시간순으로 정렬
# 처음에 종료 시간만으로 정렬해서 예외 케이스 발생함. 
schedule.sort(key = lambda x : (x[1], x[0]))

print(solution())