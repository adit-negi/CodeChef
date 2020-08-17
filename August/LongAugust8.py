t = int(input())
for i in range(t):
    N = int(input())
    graph = {}
    for i in range(N-1):
        UV = list(map(int, input().split()))
        u = int(UV[0])
        v = int(UV[1])
        if u in graph:
            graph[u].add(v)
        else:
            graph[u] = set([v])
        if v in graph:
            graph[v].add(u)
        else:
            graph[v] = set([u])
    P = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    l = []

    def dfs(graph, start, visited=None):

        if visited is None:
            visited = set()
        visited.add(start)

        l.append(start)

        for next in graph[start] - visited:
            dfs(graph, next, visited)
        return l
    output_array = [-1]*N
    for i in range(N):
        current_city = P[i]
        cities_accessible = dfs(graph, current_city)
        current_city_population = A[i]
        l = []
        for j in cities_accessible:
            index = P.index(j)
            B[index] -= min(A[i], B[index])
            if B[index] == 0:
                output_array[index] = i+1
        del graph[P[i]]
        for keys in graph:
            if P[i] in graph[keys]:
                graph[keys].remove(P[i])

    print(output_array)
