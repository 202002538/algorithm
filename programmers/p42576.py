# 해시/ 완주하지 못한 선수
from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)

    return ''.join((p - c).keys())

if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

