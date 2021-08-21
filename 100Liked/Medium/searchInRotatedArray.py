def search(nums, target):
    # 由于数组旋转了，所以原来有序的数组无序了，不能直接查找
    # 先逆序遍历，找到第一个升序的点，即为分界点，如[4,5,6,7,0,1,2]中的0
    i = len(nums) - 1
    while i > 0 and nums[i] >= nums[i-1]:
        i -= 1
    # 找到0，此时i为分界点
    # 然后拼接成有序的数组
    small = nums[i:]
    big = nums[:i]
    new_nums = small+big
    
    # 二分查找
    left = 0
    right = len(nums) - 1
    # 是否找到目标值
    tmp = -1
    while left <= right:
        mid = (left + right) // 2
        if new_nums[mid] == target:
            tmp = mid
            break
        elif new_nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # 如果找到目标值，就在原来的数组中找索引
    if tmp != -1:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
    else:
        return tmp  # 否则返回-1