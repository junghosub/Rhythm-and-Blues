def solution(n):
    answer = []
    for i in range(n-(n//2)+1):
        array = [n, (n//2)+i]
        j = 2
        while True:
            if array[j-2] - array[j-1] >= 0:
                array.append(array[j-2]-array[j-1])
                j += 1
            else:
                break
        if len(answer) < len(array):
            answer = array
    return answer

n = int(input())
print(len(solution(n)))
print(*(solution(n)))