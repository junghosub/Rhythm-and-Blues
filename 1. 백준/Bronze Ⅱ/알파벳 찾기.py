import string
S = str(input())
S = list(S)

alphabet = [] # 알파벳 리스트 만들어줌
for i in range(65,91): # 아스키 코드를 이용함
    w = chr(i).lower()
    alphabet.append(w)

print(*([-1 if j not in S else S.index(j) for j in alphabet]))