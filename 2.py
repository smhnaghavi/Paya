n, m = map(int, input("Enter the number of vertices and the number of edges: ").split())

cost, magic, edges = [-1, ], [-1, ], [-1, ]

print("Enter edges u v cost magic: ")

for i in range(m):
    u, v, c, mag = map(int, input().split())
    cost.append(c)
    magic.append(mag)
    edges.append([u, v])

b = int(input("Enter the maximum cost: "))

dp = [[0 for j in range(b+1)] for i in range(m+1)]
par = [[0 for j in range(b+1)] for i in range(m+1)]

for i in range(1, m+1):
    for j in range(b+1):
        dp[i][j] = dp[i-1][j]
        par[i][j] = False
        if j >= cost[i] and dp[i-1][j-cost[i]] + magic[i] > dp[i][j]:
            dp[i][j] = dp[i-1][j-cost[i]] + magic[i]
            par[i][j] = True

ans = []
idx = b - 1

for i in range(m, -1, -1):
    if par[i][idx]:
        idx -= cost[i]
        ans.append(edges[i])
        
print(ans)