# 완전탐색 / 카펫

def solution(brown, yellow):
    for h in range(1, yellow+1):
        if yellow % h == 0:
            if brown == 2*h + 2*(yellow//h+2):
                return [yellow//h+2, h+2]

if __name__ == '__main__':
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))
