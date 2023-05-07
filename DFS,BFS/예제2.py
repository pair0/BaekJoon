from collections import deque


# def dfs(graph, start_node, visited = []):
#     visited.append(start_node)
#
#     for node in graph[start_node]:
#         if node not in visited:
#             dfs(graph, node, visited)
#     return visited

def dfs(graph, start_node, visited = []):
    visited.append(start_node)

    for node in graph[start_node]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def bfs(graph, start_node):
    need_visited, visited = list(), list()

    need_visited = graph[start_node]

    while need_visited:

        node = need_visited[0]
        del need_visited[0]

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(dfs(graph, 'A'))