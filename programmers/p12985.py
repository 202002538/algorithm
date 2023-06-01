# 2017 팁스타운 / 예상 대진표

def isFight(a, b):
    if a-b == 1 or b-a == 1:
        if min(a, b) % 2 == 1:
            return True
    return False

def solution(n, a, b):
    round = 1
    while not isFight(a,b):
        a = (a+1) // 2
        b = (b+1) // 2
        round += 1
    return round

if __name__ == '__main__':
    print(solution(8, 4, 7))
