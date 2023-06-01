# 완전탐색 / 소수 찾기

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    if x <= 1:
        return False
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def dfs(s, numbers, l):
    if len(s) == l:
        return 1 if is_prime_number(int(s)) else 0

    elif is_prime_number(int(s)):
        answer = 1
        for n in set(numbers):
            cp_nums = numbers.copy()
            answer += dfs(s + cp_nums.pop(cp_nums.index(n)), cp_nums, l)
        return answer
    else:
        answer = 0
        for n in set(numbers):
            cp_nums = numbers.copy()
            answer += dfs(s+cp_nums.pop(cp_nums.index(n)), cp_nums, l)
        return answer

def solution(numbers):
    numbers = [n for n in numbers]
    answer = 0

    for n in set(numbers):
        if n != '0':
            cp_nums = numbers.copy()
            answer += dfs(cp_nums.pop(cp_nums.index(n)), cp_nums, len(numbers))
    return answer

if __name__ == '__main__':
    print(solution("17"))
    print(solution("011"))