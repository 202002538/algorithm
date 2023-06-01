# 완전탐색 / 최소직사각형

def solution(size):
    for i in range(len(size)):
        if size[i][0] < size[i][1]:
            size[i] = [size[i][1], size[i][0]]

    max_w = max(map(lambda x : x[0], size))
    max_h = max(map(lambda x : x[1], size))

    return max_w * max_h

if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))