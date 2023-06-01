# 탐욕법/ 체육복

def solution(n, lost, reserve):
    answer = n
    lost = sorted(lost)
    reserve = sorted(reserve)

    for i in range(n):
        if i + 1 in lost and i + 1 in reserve:
            lost.remove(i + 1)
            reserve.remove(i + 1)

    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
        else:
            answer -= 1
    return answer
if __name__ == '__main__':
    print(solution(5, [2,4], [1,3,5]))
    print(solution(5, [2,4], [3]))