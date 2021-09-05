# 내가 풀어본 코드
N = int(input())
tree = list(map(int, input().split()))
# 정렬
tree.sort(reverse=True)
# tree.insert(N, 0)

count = tree[0] + 1

for i in range(N):
    if tree[i] == tree[i+1]:
        count += 1
print(count)
# 아이디어는 맞는데 틀림..ㅜㅜ

# 구글링 해본 코드
n = int(input())
t = list(map(int, input().split()))

t.sort(reverse=True)
max_day = 0
for i in range(n):
    candidate = t[i] + i + 1
    if candidate > max_day:
        max_day = candidate

print(max_day + 1)

# 구글링 코드2
N = int(input())
tree = sorted(list(map(int, input().split())), reverse = True)
answer = 0

for i, j in enumerate(tree):
    answer = max(answer, i+j+2) #몇 번째에 심는가 + 자라는데 얼마나 걸리는가
print(answer)
