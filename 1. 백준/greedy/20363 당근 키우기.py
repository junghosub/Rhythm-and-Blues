# 햇빛 1 -> 온기 1 / 물 1 -> 수분 1
# 햇빛 10 -> 수분 -1 / 물 10 -> 온기 -1
# 아이디어 : 큰거에 먼저 몰빵하고 나머지를 채워준다. 그러면 차감하는 수만큼 다시 부어줌

carrot = list(map(int, input().split()))
carrot.sort(reverse = True)

print(carrot[0]+carrot[1]+(carrot[1]//10))