A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

# 숏코딩
A, B = map(int, input().split())
print(['><'[A < B], '=='][A==B])
#앞 부분은 리스트
#뒷 부분은 인덱스입니다.
#a가 b와 같아면 a==b 부분이 1이 되어서 '=='를,
#아닌 경우에는 0이 되어서 '><'[a<b]를 뜻하게 되고
#같은 논리로 '>'나 '<'가 출력됩니다.