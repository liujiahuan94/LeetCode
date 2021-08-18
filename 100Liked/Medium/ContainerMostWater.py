def mostWater(height):
    '''
    首先用暴力二层循环，复杂度大概是O(n^2)
    '''
    max_water = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            cur_water = (j - i) * min(height[i], height[j])
            max_water = max(max_water, cur_water)
        
    return max_water

def mostwater2(height):
    '''
    使用DP方法，“短板效应”
    基本思想是从左右两边同时向中间移动，如果左边低，那么高度取决于左边，并将左边右移；
    如果右边低，那么高度取决于右边，并将右边左移
    '''
    L, R, width, res = 0, len(height) - 1, len(height) - 1, 0

    for w in range(width, 0, -1):
        if height[L] < height[R]:
            res = max(res, height[L] * w)
            L += 1
        else:
            res = max(res, height[R] * w)
            R -= 1
    
    return res
