# 2017 팁스타운 / 짝지어 제거하기

def solution(s):
    stack = []
    for a in s:
        if stack and stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)
    return 1 if not stack else 0

if __name__ == '__main__':
    print(solution("baabaa"))
    print(solution("cdcd"))
