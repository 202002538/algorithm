# 이분탐색/ 입국심사

def solution(n, times):
    worst = max(times)*n
    best = 0
    while best <= worst:
        mid = (best + worst) // 2
        im = sum(mid//t for t in times)

        if im >= n:
            if sum((mid-1)//t for t in times) < n:
                return mid
            worst = mid-1
        else:
            best = mid+1

if __name__ == '__main__':
    print(solution(6, [7,10]))