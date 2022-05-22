max_computer_count = int(input())
graph = [[False] for _ in range(max_computer_count + 1)]
c = int(input())
count = -1

for _ in range(c):
    a, b = map(int, input().split())  
    graph[a].append(b)
    graph[b].append(a)

def dfs(val):
    global count
    if not graph[val][0]:
        count += 1
        graph[val][0] = True

        for i in range(1, len(graph[val])):
            dfs(graph[val][i])
dfs(1)
print(count)