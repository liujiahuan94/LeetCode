def moveZeros(nums):
    '''
    基本思想是，记录下序列中当前最近一个0的位置，遇到下一个不为0的数的时候就交换
    这里判断一下0的位置和当前遍历的指针的位置，防止交换了两个都不为0的数
    '''
    zero = 0 # record the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            if zero < i:
                nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1

    return nums

if __name__ == '__main__':
    nums = [1, 3, 12, 0, 1]
    re = moveZeros(nums)
    print(re)