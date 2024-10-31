def dfs(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

def can_become_complete_graph(N, edges):
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * N
    dfs(graph, 0, visited)
    
    if all(visited):
        return "NO"
    else:
        return "YES"

N = int(input())  
M = int(input())  
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u - 1, v - 1)) 

print(can_become_complete_graph(N, edges))
