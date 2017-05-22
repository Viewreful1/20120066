import sys
from collections import deque
from collections import OrderedDict
Deque = deque()
Stack = []

N, M, V = map(int, sys.stdin.readline().split())

Graph = [[] for i in range(N)]

for m in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    Graph[a].append(b)
    Graph[b].append(a)

visit = list()
result = list()


def dfs(v):
    visit[v] = True
    result.append(v + 1)
    for u in Graph[v]:
        if visit[u] is False:
            dfs(u)


def bfs(v):
    visit[v] = True
    Deque.append(v)
    while len(Deque):
        v = Deque[0]
        result.append(v + 1)
        Deque.popleft()
        for u in Graph[v]:
            if visit[u] is False:
                visit[u] = True
                Deque.append(u)

for i, l in enumerate(Graph):
    Graph[i] = list(sorted(l))

visit = [False for i in range(N)]
result = []
dfs(V - 1)
sys.stdout.write(" ".join(map(str, result)) + '\n')
result = []
visit = [False for i in range(N)]
bfs(V - 1)
sys.stdout.write(" ".join(map(str, result)) + '\n')