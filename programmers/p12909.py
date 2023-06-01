# 스택,큐 / 올바른 괄호

def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            try:
                stack.pop()
            except IndexError:
                return False

    return False if stack else True

if __name__ == '__main__':
    print(solution("()()"))
    print(solution("(())()"))
    print(solution(")()("))
    print(solution(")()("))
