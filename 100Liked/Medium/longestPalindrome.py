def longestPalindrome(s: str) -> str:
    
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