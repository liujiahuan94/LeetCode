def uniquePaths(m, n):
    # m行n列
    # 平安果问题，就是普通的动态规划
    dp_table = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        dp_table[i][0] = 1
    
    for i in range(n):
        dp_table[0][i] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            dp_table[i][j] = dp_table[i-1][j] + dp_table[i][j-1]
    
    return dp_table[-1][-1]