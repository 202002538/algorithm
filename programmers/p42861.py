# 탐욕법/ 섬 연결하기

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    answer = 0

    vertices = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[2])

    parent = [0] * n
    for node in vertices:
        parent[node] = node

    for edge in costs:
        v, u, cost = edge
        if find_parent(parent, v) != find_parent(parent, u):
            union_parent(parent, v, u)
            answer += cost

    return answer

if __name__ == '__main__':
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))