#정렬/ H-Index

def solution(citations):
    answer = 0
    citations = sorted(citations) #[0, 1, 3, 5, 6]
    for i in range(1, len(citations)+1):
        freq = sum(list(map(lambda x : x >= i, citations)))
        if freq >= i: answer = i
        else: break
    return answer

if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]))