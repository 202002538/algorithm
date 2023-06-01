# 스택,큐 / 기능개발
import math

def solution(prog, speeds):
    answer = []

    while prog:
        count = 0
        day = math.ceil((100 - prog[0]) / speeds[0])  # 맨 앞 기능을 개발하기위해 소요되는 일수
        prog = [prog[j] + day * speeds[j] for j in range(len(speeds))]
        while prog and prog[0] >= 100:
            prog.pop(0)
            speeds.pop(0)
            count += 1
        answer.append(count)

    return answer

if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))