# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python

from collections import deque

def solution(n, edge):
    graph = [[] for i in range(n + 1)]

    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
        print(x, y, graph)
    answer = [0 for _ in range(n + 1)]
    queue = deque([1])
    print(queue)

    answer[1] = 1
    while queue:
        node = queue.popleft()
        for g in graph[node]:
            if answer[g] == 0:
                queue.append(g)
                answer[g] = answer[node] + 1

    return answer.count(max(answer))

# from collections import deque
# def solution(n, edge):
#     answer = 0

#     # graph = [[] for i in range(n + 1)]
#     graph_list = [[] for _ in range(n + 1)]

#     for a, b in edge:
#         graph_list[a].append(b)
#         graph_list[b].append(a)
#         print(a, b, graph_list)

#     answer = [0 for _ in range(n + 1)]
#     queue = deque([1])

#     while queue:
#         val = queue.popleft()

#         for i in graph_list[val]:
#             if answer[i] == 0:
#                 answer[i] = answer[val] + 1
#                 queue.append(i)

#     # return answer.count(max(answer))
#     print(answer)


#     return answer