import sys

input = sys.stdin.readline

def solution(graph, removeNode):
    
    if len(graph[removeNode]) == 1: #지울 노드가 리프 노드일 경우 브레이크
        graph[removeNode].remove(removeNode)
        return

    for i in range(1, len(graph[removeNode])):
        removelist.append(graph[removeNode][i])
        solution(graph, graph[removeNode][i])
        

if __name__ == "__main__":
    N = int(input())
    chain = list(map(int, input().split()))
    graph = [[i] for i in range(N)] 
    
    answer = 0

    for i in range(N):
        if chain[i] != -1:
            graph[chain[i]].append(i)

    removeNode = int(input())
    removelist = [removeNode]
    solution(graph, removeNode)

    for i in range(len(graph)):
        for j in removelist:
            if j in graph[i]:
                graph[i].remove(j)

    for i in graph:
        if len(i) == 1:
            answer += 1

    print(answer)