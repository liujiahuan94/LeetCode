def searchRange(nums, target):
    # 想法是先用二分法找目标值，如果没找到直接返回-1，-1
    # 如果找到了就直接暴力循环，找最高值和目标值的个数，返回[最高值-个数+1, 最高值]
    def find(num, t):
        left = 0
        right = len(num) - 1
        while left <= right:
            mid = (left + right) // 2
            if num[mid] == t:
                return mid
            elif num[mid] > t:
                right = mid - 1
            else:
                left = mid + 1
        return None
    
    if not nums:
        return [-1, -1]
    
    first_try = find(nums, target)
    if first_try is None:
        return [-1, -1]
    else:
        count = 0
        high = -1
        for i in range(len(nums)):
            if nums[i] == target:
                count += 1
                high = i
        
        return [high-count+1, high]