def jump(nums):
    # 不是很懂，贪心算法
    # 每次找下一次跳跃能到达最远的距离的那个位置
    cur_step = next_step = jump = 0
    
    for i in range(len(nums)):
        if cur_step < i:
            jump += 1
            cur_step = next_step
        
        next_step = max(next_step, i+nums[i])
    
    return jump