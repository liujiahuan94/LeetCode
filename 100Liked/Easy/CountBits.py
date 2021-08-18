def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    基本思路是2进制表示的数可以以2为单位扩展，例如0区间加1为到1区间
    [0,1]加1位到[2,3]；[0,3]加1位到[4,7]；[0,7]加1位到[8,15]
    因此可以以2倍的形式扩展列表
    """

    res = [0]
    while len(res) <= num:
        res += [i+1 for i in res] # 2倍形式扩展
    return res[:num+1]

def countBits(num):
    '''
    用到著名的Brian Kernighan算法，看一个数是不是2的指数
    '''
    setBits = [0] * (num+1)
    # (i & (i -1)) is actually Brian Kernighan’s Algorithm, so always keep it handy for counting ones
    for i in range(1 ,num+1):
        setBits[i] = setBits[i & (i-1)] + 1
    return setBits


if __name__ == '__main__':
    re = countBits(5)
    print(re)