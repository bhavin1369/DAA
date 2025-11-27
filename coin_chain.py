def coin(coins, amt):
    n = len(coins)
    T = [[float('inf')] * (amt + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        T[i][0] = 0
    for i in range(1, n + 1):
        for j in range(1, amt + 1):
            if j < coins[i - 1]:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = min(1 + T[i][j - coins[i - 1]], T[i - 1][j])
    return -1 if T[n][amt] == float('inf') else T[n][amt]

coins = [1, 5, 6, 8]
amt = 11
print(coin(coins, amt))

