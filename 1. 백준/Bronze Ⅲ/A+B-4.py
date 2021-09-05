while(True):
    try:
        A, B = map(int, input().split())
        if A > 0 and B < 10:
            print(A + B)
    except:
        break

# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.