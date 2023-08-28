def solution(skill, skill_trees):
    for index, tree in enumerate(skill_trees):
        skill_trees[index] = ''.join(list(map(lambda x: x if x in skill else "", tree)))

    answer = 0
    for sk in skill_trees:
        if skill.startswith(sk):
            answer += 1

    return answer