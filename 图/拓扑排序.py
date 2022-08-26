from collections import defaultdict

def main():

    n = 5
    vectors = [[1,2], [1,3], [1,4],[2,5],[3,2],[4,2]]


    outwards = defaultdict(list)
    inwards = defaultdict(list)

    for x,y in vectors:
        outwards[x].append(y)
        inwards[y].append(x)
    print(outwards)
    print(inwards)
    begin_list = []
    visited = [False] * n
    for i in range(1, n + 1):
        if i not in inwards.keys():
            begin_list.append(i)


    def dfs(i):
        visited[i - 1] = True
        print(i, end=' ')
        for nxt_pt in outwards[i]:
            if not visited[nxt_pt - 1]:
                inwards[nxt_pt].remove(i)
                if not inwards[nxt_pt]:
                    dfs(nxt_pt)


    for begin_pt in begin_list:
        dfs(begin_pt)

def main2():
    import sys
    n, m = list(map(int, next(sys.stdin).strip().split(' ')))

    from collections import defaultdict

    class Graph:
        def __init__(self, vertices):
            self.graph = defaultdict(list)
            self.V = vertices

        def addEdge(self, u, v):
            self.graph[u].append(v)

        def topologicalSortUtil(self, v, visited, stack):

            visited[v] = True

            for i in self.graph[v]:
                if visited[i] == False:
                    self.topologicalSortUtil(i, visited, stack)

            stack.insert(0, v)

        def topologicalSort(self):
            visited = [False] * self.V
            stack = []

            for i in range(self.V):
                if visited[i] == False:
                    self.topologicalSortUtil(i, visited, stack)

            return stack

    graph = Graph(n)
    for line in sys.stdin:
        x, y = list(map(int, line.strip().split(' ')))
        graph.addEdge(x - 1, y - 1)

    for num in graph.topologicalSort():
        print(num + 1, end=' ')


if __name__ == '__main__':
    main()