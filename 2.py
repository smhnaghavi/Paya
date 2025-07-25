# Q2
# Solution in O(n * b)

try:
    n = int(input("Enter n: "))
    cost, magicvalue = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
    cost = list(map(int, input("Enter costs list: ").split()))
    magicValue = list(map(int, input("Enter magic values: ").split()))
    b = int(input("Enter the maximum cost: "))
except ValueError:
    print("Invalid Input!")
    exit()

dp = [[-1 for _ in range(b+1)] for _ in range(n+1)]

ans = 0
for i in range(1, n+1):
    for j in range(1, b+1):
        if (j - cost[i]) >= 0 and dp[i-1][j-cost[i]] != -1:
            dp[i][j] = dp[i - 1][j-cost[i]] + magicvalue[i]
            ans = max(ans, dp[i][j])
        
print(ans)