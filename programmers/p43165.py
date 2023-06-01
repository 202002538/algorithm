#깊이,너비 우선 탐색/ 타겟 넘버

def dfs(numbers, target, i, total):
    if i == len(numbers):
        return 1 if total == target else 0
    else:
        return dfs(numbers, target, i+1, total+numbers[i]) + dfs(numbers, target, i+1, total-numbers[i])

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer

if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))