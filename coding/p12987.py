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