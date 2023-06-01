# 스택,큐 / 같은 숫자는 싫어

def solution(arr):
    answer = [arr[0]]
    for i in arr[1:]:
        if answer[-1] != i:
            answer.append(i)
    return answer

if __name__ == '__main__':
    print(solution([1,1,3,3,0,1,1]))
    print(solution([4,4,4,3,3]))