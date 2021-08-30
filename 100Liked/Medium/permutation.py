def permute(nums):
    # 标准回溯算法
    # 框架为，先设置终止条件，把结果加进去，然后返回
    # 循环选择列表，路径做出选择，接着递归，然后撤销选择
    res = []
    def backTrack(path, remain):
        if not remain:
            res.append(path[:])
            return
        
        for i in range(len(remain)):
            path.append(remain[i])
            backTrack(path, remain[:i]+remain[i+1:])
            path.pop()
    
    backTrack([], nums)
    
    return res