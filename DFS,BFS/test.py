def test(graph):
    graph[1] = 3

if __name__ == "__main__":
    graph = [1, 2, 3]

    test(graph)

    print(graph)