# 힙 / 디스크 컨트롤러
import heapq

def solution(jobs):
    # 요청 시간 오름차순으로 정렬된 리스트
    # 현재 시점에 요청되어있는 작업만 힙에 추가(이때 소요시간 오름차순)
    jobs.sort()

    leng = len(jobs)
    total, now = 0, 0
    able = []

    while True:
        while jobs and jobs[0][0] <= now:
            heapq.heappush(able, jobs.pop(0)[::-1])

        if able:  # 지금 할 수 있는 작업이 남아있으면.
            need, request = heapq.heappop(able)
            now += need
            total += (now - request)

        else:
            if not jobs:
                break
            else:
                now = jobs[0][0]
                heapq.heappush(able, jobs.pop(0)[::-1])

    return total // leng

if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]))