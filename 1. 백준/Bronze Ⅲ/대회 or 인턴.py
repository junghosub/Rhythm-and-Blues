# 여자 2, 남자 1, 인턴쉽은 k명
# 인원이 더욱 많은 성별에서 1명씩 제외
woman, man, k = map(int, input().split())

for _ in range(k):
    if woman //2 > man:
        woman -= 1
    else:
        man -= 1
print(min(woman//2, man))