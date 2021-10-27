import sys

n = int(sys.stdin.readline()) # 사진틀의 개수
votes = int(sys.stdin.readline()) # 총 추천 횟수
student = list(map(int, sys.stdin.readline().split())) # 추천 받은 학생

frame = dict() # 추천하기 전 사진틀은 비어있다.

for no, vote in enumerate(student):
    if len(frame) < n: # 사진틀이 비어있는 경우
        if vote in frame: # 이미 추천을 받은 경우
            frame[vote][0] += 1 # 추천 수 += 1
        else: # 추천을 받지 않은 경우
            frame[vote] = [1, no] # 투표 수, 게시된 수
    else: # 사진틀이 가득 찬 경우
        if vote in frame: # 이미 추천을 받은 경우
            frame[vote][0] += 1
        else: # 추천을 받지 않은 경우
            frame = dict(sorted(frame.values(), reverse=True, key = lambda x : x[1][0]))
            frame.popitem()
print(frame)