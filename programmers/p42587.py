# 스택,큐 / 프로세스

def solution(prior, location):
    printed = []
    for i, p in enumerate(prior):
        prior[i] = [i, p]

    while len(prior) > 1:
        i, p = prior.pop(0)
        if p >= max(prior, key=lambda x: x[1])[1]:
            if i == location:
                return len(printed)+1
            printed.append(i)
        else:
            prior.append([i, p])

    return len(printed)+1

if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
