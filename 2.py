n = int(input("Enter n: "))
cost = list(map(int, input("Enter costs list: ").split()))
magic = list(map(int, input("Enter magic values: ").split()))
b = int(input("Enter the maximum cost: "))

dp = [-1 for _ in range(b+1)]
dp[0] = 0

ans = 0
for i in range(1, n+1):
    for j in range(b, cost[i]-1, -1):
        if j - cost[i] != -1:
            dp[j] = max(dp[j], dp[j-cost[i]] + magic[i])
            ans = max(ans, dp[j])
        
print(ans)