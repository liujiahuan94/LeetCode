def twosum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    rev_table = {}
    for i, num in enumerate(nums):
        another_add = target - num
        if num in rev_table:
            return [rev_table[num], i]
        else:
            rev_table[another_add] = i


def twosum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    rev_table = {}
    for i, num in enumerate(nums):
        another_add = target - num
        if another_add in rev_table:
            return [rev_table[another_add], i]
        else:
            rev_table[num] = i


if __name__ == '__main__':
    re = twosum2([1, 2, 3, 6], 7)
    print(re)

