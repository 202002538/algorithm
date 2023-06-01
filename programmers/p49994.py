# Summer/Winter Coding(~2018) / 스킬트리

def solution(skill, skill_trees):
    for index, tree in enumerate(skill_trees):
        skill_trees[index] = ''.join(list(map(lambda x: x if x in skill else "", tree)))

    answer = 0
    for sk in skill_trees:
        if skill.startswith(sk):
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))