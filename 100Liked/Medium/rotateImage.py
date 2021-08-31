def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    # 顺时针旋转矩阵，不让使用额外的空间，只能原地交换
    # 思路为分两步，第一步将矩阵转置，第二部将矩阵中的每一行都逆序，过程可以自己推导
    # 关键点：（1）转置的时候，j的=取值范围是从i+1开始，不能从0开始，即只能交换对角线一侧的元素
    # 否则就交换了两次，转置之后又转置回来了，相当于没变
    # （2）逆序的时候，还是只交换一半的元素，否则又变回来了
    
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        for j in range(n//2):
            matrix[i][n-1-j], matrix[i][j] = matrix[i][j], matrix[i][n-1-j]