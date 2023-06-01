# 깊이,너비 우선 탐색/ 여행경로

from collections import defaultdict

def solution(tickets):
    way = []
    dic = defaultdict(list)

    for [src, dst] in tickets:
        dic[src].append(dst)
    for k in dic.keys():
        dic[k].sort(reverse=True)

    def dfs():
        stack = ["ICN"]
        while stack:
            src = stack[-1]
            if not dic[src]:
                way.append(stack.pop())
            else:
                stack.append((dic[src].pop()))

    dfs()
    return way[::-1]

if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
