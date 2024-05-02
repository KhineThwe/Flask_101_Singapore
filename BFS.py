from collections import deque

def BFS(graph, visited, start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        current = q.popleft()
        print(current, end=' ')

        for adjNode in graph[current]:
            if not visited[adjNode]:
                visited[adjNode] = True
                q.append(adjNode)

graph = {0: [1, 2],
         1: [0, 3, 4],
         2: [0],
         3: [1],
         4: [1, 5],
         5: [4]}
visited = {i: False for i in range(6)}

print("BFS traversal starting from vertex 0:", end=' ')
BFS(graph, visited, 0)