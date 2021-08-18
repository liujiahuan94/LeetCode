def longestPalindrome(s: str) -> str:
    # 找最长的回文子串，使用中心扩散法，首先定义一个扩散函数，从左右开始向两边扩散
    # 终止条件是左右都越界
    # 注意返回长度是right-left-1，因为到达最后一个判定之后，左右都又扩散了一次
    # 这里还要返回左指针作为起始点
    def centerSpread(string, left, right):
        while left >= 0 and right < len(string):
            if string[left] == string[right]:
                left -= 1
                right += 1
            else:
                break
        return right - left-1, left+1
    
    max_len = 1
    max_left = 0
    for i in range(0, len(s)-1):
        # 中心扩散分为奇数长度子串和偶数长度子串进行扩散
        odd_len, odd_left = centerSpread(s, i, i)
        even_len, even_left = centerSpread(s, i, i+1)
        if odd_len >= even_len:
            cur_len = odd_len
            cur_left = odd_left
        else:
            cur_len = even_len
            cur_left = even_left
        
        if cur_len >= max_len:
            max_len = cur_len
            max_left = cur_left
    
    return s[max_left:max_left+max_len]


if __name__ == '__main__':
    re = longestPalindrome("babad")
    print(re)