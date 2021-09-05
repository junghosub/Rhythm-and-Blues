T= int(input())

for i in range(T):
    R, S = input().split()
    print(*(int(R)*S[j] for j in range(len(S))), sep = '')
    # sep = ''을 통해 공백 없이 출력