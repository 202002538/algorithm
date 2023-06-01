# 탐욕법/ 구명보트
from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    answer = 0

    while len(people) > 1:
        p = people.pop()
        if people[0] + p <= limit:
            people.popleft()
        answer += 1
    if people:
        answer += 1
    return answer

if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))
    print(solution([70, 80, 50], 100))