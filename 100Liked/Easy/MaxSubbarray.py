class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        
        for i in range(1, length):
            maxsum = max(nums[i] + nums[i-1], nums[i])
            nums[i] = maxsum
            # nums[i] += max(nums[i-1], 0)
        
        return max(nums)