from collections import defaultdict

N = 1000
g = defaultdict(list)
n, P = map(int, input().split())
dpD = [[-1] * N for _ in range(N)]
dpU = [[-1] * N for _ in range(N)]

def DFS1(v, p):
    for u, w in g[v]:
        if u != p:
            DFS1(u, v)

    for u, w in g[v]:
        if u != p:
            for i in range(P):
                if dpD[u][i] != -1:
                    dpD[v][(i + w) % P] = max(dpD[v][(i + w) % P], dpD[u][i] + 1)

def DFS2(v, p):
    vc = [[] for _ in range(P)]

    for i in range(P):
        for u, w in g[v]:
            if u == p:
                vc[i].append((dpU[v][i], p))
                vc[i].sort()
                if len(vc[i]) > 2:
                    vc[i][0] = vc[i][1]
                    vc[i][1] = vc[i][2]
                    vc[i].pop()
            else:
                vc[(i + w) % P].append((dpD[u][i] + 1 if dpD[u][i] != -1 else -1, u))
                vc[(i + w) % P].sort()
                if len(vc[(i + w) % P]) > 2:
                    vc[(i + w) % P][0] = vc[(i + w) % P][1]
                    vc[(i + w) % P][1] = vc[(i + w) % P][2]
                    vc[(i + w) % P].pop()

    for i in range(P):
        for u, w in g[v]:
            if u != p:
                if vc[i][-1][1] == u:
                    dpU[u][(i + w) % P] = vc[i][-2][0]
                else:
                    dpU[u][(i + w) % P] = vc[i][-1][0]

                if dpU[u][(i + w) % P] != -1:
                    dpU[u][(i + w) % P] += 1
                if i == 0:
                    dpU[u][w] = max(1, dpU[u][w])

    for u, w in g[v]:
        if u != p:
            DFS2(u, v)

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

for i in range(1, n + 1):
    dpD[i][0] = dpU[i][0] = 0

DFS1(1, 1)

DFS2(1, 1)

for i in range(1, n + 1):
    print(max(dpD[i][0], dpU[i][0]), end=' ')
