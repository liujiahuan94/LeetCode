def groupAnagrams(strs):
    # 获取同分异构词
    # 基本思想是，新建一个字典存储结果。
    # 以每个词的有序排列（要排序）为键，以当前词和这个键之前的值得组合为新的值
    # 最后返回这个字典的所有值即可
    d = {}
    for w in strs:
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    
    return list(d.values())