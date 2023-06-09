# 해시/ 의상
from collections import Counter

def solution(clothes):
    clothes = list(type for cloth, type in clothes)
    hash = Counter(clothes)
    answer = 1

    for i in hash.values():
        answer *= (i+1)

    return answer-1

if __name__ == '__main__':
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))