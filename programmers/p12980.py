# Summer/Winter Coding(~2018) / 점프와 순간 이동

def solution(n):
    power = 0

    while n != 0:
        while n % 2 == 0: #계속 나누기
            n /= 2
        #홀수가 되는 지점에서는 점프 한칸
        power += 1
        n -= 1

    return power

if __name__ == '__main__':
    print(solution(5))
    print(solution(6))
    print(solution(5000))
