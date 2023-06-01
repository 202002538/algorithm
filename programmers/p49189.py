# 그래프/ 가장 먼 노드
from collections import deque
from collections import defaultdict

def solution(n, edge):
    dic = defaultdict(list)  # 디폴트값이 list인 딕셔너리
    visited = [1] + [0] * (n - 1)  # 방문여부 리스트

    for u, v in edge:
        dic[u].append(v)
        dic[v].append(u)  # 양방향

    def bfs():
        q = deque([1])
        while q:
            new_q = deque([])
            for j in q:
                for i in dic[j]:
                    if visited[i - 1] == 0:
                        new_q.append(i)
                        visited[i - 1] = 1
            if len(new_q) == 0:
                return len(q)
                break
            else:
                q = new_q
        return 0

    return bfs()

if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))