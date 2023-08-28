from heapq import heappush

def solution(dirs):
    heap = []
    now_r, now_c = 0, 0

    for d in dirs:
        if d == "U" and now_r-1 >= -5:
            heappush(heap, [now_r, now_c, now_r-1, now_c])
            heappush(heap, [now_r - 1, now_c, now_r, now_c])
            now_r -= 1
        elif d == "D" and now_r+1 <= 5:
            heappush(heap, [now_r, now_c, now_r+1, now_c])
            heappush(heap, [now_r + 1, now_c, now_r, now_c])
            now_r += 1
        elif d == "L" and now_c-1 >= -5:
            heappush(heap, [now_r, now_c, now_r, now_c-1])
            heappush(heap, [now_r, now_c-1, now_r, now_c])
            now_c -= 1
        elif d == "R" and now_c+1 <= 5:
            heappush(heap, [now_r, now_c, now_r, now_c+1])
            heappush(heap, [now_r, now_c+1, now_r, now_c])
            now_c += 1

    answer = 0
    while heap:
        h = heap.pop()
        if heap.count(h) == 0:
            answer += 1

    return answer // 2