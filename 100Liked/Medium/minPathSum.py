def minPathSum(grid):
    # 最小和的路径，只能向右向下走
    # m行n列
    # 还是平安果动态规划题，第一行和第一列是固定的
    # 其他格子是当前格子值加上来自上方和左侧的dp值的最小值
    m = len(grid)
    n = len(grid[0])
    dp_table = [[0 for _ in range(n)] for _ in range(m)]
    dp_table[0][0] = grid[0][0]
    for i in range(1, m):
        dp_table[i][0] = dp_table[i-1][0] + grid[i][0]
    
    for i in range(1, n):
        dp_table[0][i] = dp_table[0][i-1] + grid[0][i]
    
    for i in range(1, m):
        for j in range(1, n):
            dp_table[i][j] = grid[i][j] + min(dp_table[i-1][j], dp_table[i][j-1])
    
    return dp_table[-1][-1]