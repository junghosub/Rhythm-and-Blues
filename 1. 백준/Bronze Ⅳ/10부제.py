# 일의 자리를 입력받고, count() 함수를 통해 위반한 자동차의 대수 출력
day = int(input())
car_numbers = list(map(int, input().split()))
print(car_numbers.count(day))