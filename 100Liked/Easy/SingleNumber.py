def singleNumber(nums: List[int]) -> int:
    if len(nums) < 2:
        return nums[0]
    
    result = 0
    for i in nums:
        result = result ^ i
    
    return result