def findSubString(s):
    # 使用一个字典维护已经使用过的字符及其对应的位置
    # 这里的关键是开始位置的更改
    # 如果字符串已经用过了，in used，并且目前的字符串起始点<=这个用过的字符对应的位置
    # 即这个字符串重复了，所以起始点就要跳过这个字符，即从上一个这个字符的后一个位置重新开始
    # 这里判断start <= used[c]的目的是，如果起始点在这个重复字符串的后面，那就没必要跳过它了
    # 如果更改了起始点，结果会变成，不对
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)  # 如果字符串没用过，及时更新最长的长度即可
        
        used[c] = i
    
    return max_length


if __name__ == '__main__':
    print(findSubString('abcabcbb'))