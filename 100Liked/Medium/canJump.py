def canJump(nums):
    # 目的是跳跃到终点，只用判断有无
    # 使用贪心算法，即计算从当前位置能跳到的最远位置
    # 然后在每个位置都更新这个最远距离
    # 如果最远距离大于数组长度-1（索引减1），那么就可以到达
    # 剪枝条件：如果当前索引位置大于最大距离了，就没必要循环了，因为达到不了
    
    total, farthest = len(nums), 0
    for i in range(total):
        if i <= farthest:
            farthest = max(farthest, i+nums[i])
            if farthest >= total-1:
                return True
    
    return False