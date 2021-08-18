def findDisappearedNumbers(nums):
    '''
    基本思想是遍历数组的时候，将出现过的数组对应的索引(注意减1)处的数字置为负的
    这里需要注意的是两个绝对值得使用，因为遍历前面的数字的时候可能把后面的数字置为负
    后面再遍历它的时候就成负的了，要用绝对值改回来。其次，第二个就是赋值的时候的绝对值
    就是防止原来的数字已经是负的了，因此有可能这个数字已经出现过了。
    注意这里只能改成负值，改成其他的都会导致信息的丢失
    '''
    for num in nums:
        index = abs(num) - 1
        nums[index] = - abs(nums[index])
            
    return [i + 1 for i, num in enumerate(nums) if num > 0]


if __name__ == '__main__':
    re = findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print(re)