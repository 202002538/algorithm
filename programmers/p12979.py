# Summer/Winter Coding(~2018) / 기지국 설치

def solution(n, stations, w):
    gap_list = []
    now = 1
    for index, s in enumerate(stations):
        gap = (s-w) - now
        if gap >= 0:
            gap_list.append(gap)
        now = s + w + 1
        if index == len(stations)-1 and s+w < n:
            gap_list.append(n -(s+w))


    answer = 0
    for gap in gap_list:
        if gap % (2*w+1) == 0:
            answer += gap // (2*w+1)
        else:
            answer += max(1, (gap // (2*w+1))+1)
    return answer

if __name__ == '__main__':
    print(solution(11, [4, 11], 1))
    print(solution(16, [9], 2))

