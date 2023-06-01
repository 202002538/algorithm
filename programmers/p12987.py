# Summer/Winter Coding(~2018) / 숫자 게임
from collections import deque

def solution(A, B):
    Aq = deque(sorted(A))
    Bq = deque(sorted(B))

    answer = 0
    while Bq and Aq:
        a = Aq.popleft()
        b = Bq.popleft()
        if a < b:
            answer += 1
        else:
            Aq.insert(0, a)
    return answer

if __name__ == '__main__':
    print(solution([5,1,3,7], [2,2,6,8]))
    print(solution([2,2,2,2], [1,1,1,1]))