#동적계획법/ 도둑질

def dp(money_list):
    #bottom_up방식 사용
    money_list[1] = max(money_list[0], money_list[1])
    for i in range(2, len(money_list)):
        money_list[i] = max(money_list[i-1], money_list[i-2] + money_list[i])
    return max(money_list)

def solution(money):
    money_first = money[0:-1] #시작을 고려하되 마지막을 선택하지 않는 경우
    money_last = money[1:] #마지막을 고려하되 시작을 선택하지 않는 경우
    answer = max(dp(money_first), dp(money_last))
    return answer

if __name__ == '__main__':
    print(solution([1, 2, 3, 1]))