# Summer/Winter Coding(2019) / 멀쩡한 사각형
import math

def solution(w, h):
    divider = math.gcd(w, h)
    divided_w = w / divider
    divided_h = h / divider

    return w * h - divider * (divided_w + divided_h -1)

if __name__ == '__main__':
    print(solution(8, 12))
