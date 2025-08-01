n = int(input("Enter the number of vertices of tree: "))
N = 10**5 + 10
G = [[] for _ in range(N)]
chld = [[] for _ in range(N)]
val = [0] * N
dp0 = [0] * N
dp1 = [0] * N
par = [0] * N
mark = [False] * N

print("Enter the edges of tree u v: ")
for _ in range(n - 1):
    v, u = map(int, input().split())
    G[v].append(u)
    G[u].append(v)

val_input = list(map(int, input().split()))
for i in range(n):
    val[i + 1] = val_input[i]

def upd(v):
    dp0[v] = 0
    dp1[v] = val[v]
    for u in chld[v]:
        dp1[v] += dp0[u]
        dp0[v] += max(dp0[u], dp1[u])

def DFS(v):
    mark[v] = True
    for u in G[v]:
        if not mark[u]:
            par[u] = v
            chld[v].append(u)
            DFS(u)
    upd(v)

DFS(1)

q = int(input("Enter the number of queries: "))
for _ in range(q):
    v, w = map(int, input("Update u v: ").split())
    val[v] = w
    while v != 0:
        upd(v)
        v = par[v]
    print(max(dp0[1], dp1[1]))
