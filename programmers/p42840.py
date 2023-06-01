# 완전탐색 / 모의고사

def solution(answers):
    people = {'p1' : [1,2,3,4,5], 'p2': [2,1,2,3,2,4,2,5], 'p3': [3,3,1,1,2,2,4,4,5,5]}
    correct = [0, 0, 0]

    for i, ans in enumerate(answers):
        if ans == people['p1'][i % len(people['p1'])]:
            correct[0] += 1
        if ans == people['p2'][i % len(people['p2'])]:
            correct[1] += 1
        if ans == people['p3'][i % len(people['p3'])]:
            correct[2] += 1

    answer = []
    for i, c in enumerate(correct):
        if c == max(correct):
            answer.append(i+1)

    return answer

if __name__ == '__main__':
    print(solution([1,2,3,4,5]))
    print(solution([1,3,2,4,2]))
