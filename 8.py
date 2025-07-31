N = 200010

adj = [set() for _ in range(N)]
radj = [set() for _ in range(N)]
visited = [0] * N
topol = []
ok = True

def DFS(v):
    global ok, topol
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

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].add(v)
    radj[v].add(u)

for _ in range(q):
    parts = input().split()
    t = parts[0]
    u, v = map(int, parts[1:])
    
    if t == '+':
        adj[u].add(v)
        radj[v].add(u)
    else:
        if v in adj[u]:
            adj[u].remove(v)
        if u in radj[v]:
            radj[v].remove(u)
    
    visited = [0] * (n + 1)
    topol = []
    ok = True
    
    for i in range(1, n + 1):
        if not visited[i]:
            DFS(i)
    
    if ok:
        print("Yes")
        print(' '.join(map(str, reversed(topol))))
    else:
        print("No")
