def subsets(nums):
    # 有点像另类的斐波那契数列
    # 假设是123
    # 最开始result中是[]
    # 从1开始遍历，结果是[]+[1]=[1]
    # 然后是2，结果是[]+[2]=[2], [1]+[2]=[1,2]
    # 然后是3，结果是[]+[3]=[3], [1]+[3]=[1,3], [2]+[3]=[2,3], [1,2]+[3]=[1,2,3]
    # 因为要求子集无重复，所以可以这么依次相加
    
    result = [[]]
    for number in nums:
        for i in result:
            # append (i in result list + number) to result list
            result = result +[i + [number]]
    return result