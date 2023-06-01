# 월간 코드 챌린지 시즌2 / 괄호 회전하기

def isgood(s):
    stack = []
    while s:
        paren = s.pop(0)
        if paren == ']':
            if not stack or stack.pop() != '[':
                return False
        elif paren == ')':
            if not stack or stack.pop() != '(':
                return False
        elif paren == '}':
            if not stack or stack.pop() != '{':
                return False
        else:
            stack.append(paren)
    return True if not stack else False

def solution(s):
    s = list(s)
    count = 0

    for i in range(len(s)):
        s = s[1:] + [s[0]]
        if isgood(s.copy()):
            count += 1

    return count

if __name__ == '__main__':
    print(solution("[](){}"))
    print(solution("}]()[{"))
    print(solution("[)(]"))
    print(solution("}}}"))