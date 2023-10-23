from collections import deque


def biggest_dist(graph, node):
    used = set()
    que = deque()
    que.append(node)
    dist = [0] * (n1 + n2 + 1)
    used.add(node)
    while que:
        x = que.popleft()
        for n in graph[x]:
            if n not in used:
                used.add(n)
                que.append(n)
                dist[n] = dist[x] + 1
    return max(dist)


n1, n2, m = map(int, input().split())

graph_1 = {i: set() for i in range(1, n1+1)}
graph_2 = {i: set() for i in range(n1+1, n1+n2+1)}

for i in range(m):
    a, b = map(int, input().split())
    if a <= n1:
        if not a in graph_1.keys():
            graph_1[a] = set()
        graph_1[a].add(b)
        if not b in graph_1.keys():
            graph_1[b] = set()
        graph_1[b].add(a)
    else:
        if not a in graph_2.keys():
            graph_2[a] = set()
        graph_2[a].add(b)
        if not b in graph_2.keys():
            graph_2[b] = set()
        graph_2[b].add(a)

print(biggest_dist(graph_1, 1) + biggest_dist(graph_2, n1 + n2) + 1)
