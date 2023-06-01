# 힙 / 더 맵게
import heapq

def solution(scoville, K):
    heapq.heapify(scoville) #이미 원소가 들어있는 리스트를 힙으로 만듦
    answer = 0

    if scoville[0] >= K:
        return answer

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        answer += 1

    return answer

if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))
