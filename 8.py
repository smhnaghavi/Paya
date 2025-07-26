from collections import defaultdict

N = 200010

adj = defaultdict(set)
radj = defaultdict(set)
visited = [0] * N
topol = []
ok = True

def DFS(v):
    global ok
    visited[v] = 1

    for u in adj[v]:
        if not visited[u]:
            DFS(u)

    for u in radj[v]:
        if visited[u] > 1:
            ok = False

    visited[v] += 1
    topol.append(v)

n, m, q = map(int, input().split())

for i in range(m):
    u, v = map(int, input().split())
    adj[u].add(v)
    radj[v].add(u)

for i in range(q):
    t, u, v = input().split()
    u, v = int(u), int(v)

    if t == '+':
        adj[u].add(v)
        radj[v].add(u)
    else:
        adj[u].discard(v)
        radj[v].discard(u)

    visited[:] = [0] * (n + 1)
    topol.clear()
    ok = True

    for i in range(1, n + 1):
        if not visited[i]:
            DFS(i)

    if ok:
        print("Yes")
        print(' '.join(map(str, topol[::-1])))
    else:
        print("No")

