import sys
n = int(sys.stdin.readline())

queue = []

for _ in range(n):
    cmd = sys.stdin.readline().split() # 명령 받기

    if cmd[0] == 'push': # append()를 사용하여 queue에 데이터 추가
        queue.append(cmd[1])
    elif cmd[0] == 'pop': # pop(0)을 사용하여 맨 앞에 데이터를 제거 후 출력. 만약 queue가 빈 리스트라면 -1 출력
        print(queue.pop(0) if queue else -1)
    elif cmd[0] == 'size': # len() 함수를 이용하여 큐에 쌓인 데이터의 개수 출력
        print(len(queue))
    elif cmd[0] == 'empty': # queue가 빈 리스트라면 1 아니라면 0
        print(0 if queue else 1)
    elif cmd[0] == 'front': # 맨 앞인 0번째 인덱스 값 출력. 만약 빈 리스트라면 -1 출력
        print(queue[0] if queue else -1)
    else: # 맨 뒤의 -1번째 인덱스 값 출력. 만약 빈 리스트라면 -1 출력
        print(queue[-1] if queue else -1)