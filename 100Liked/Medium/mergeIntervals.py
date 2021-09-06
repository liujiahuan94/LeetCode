def mergeIntervals(intervals):
    # 合并区间
    # 首先将区间按起始位置升序排序
    # 然后从第二个位置开始遍历
    # 如果第i个区间的起点比第i-1个区间的终点大，说明不能合并，说明第i-1个区间是“干净的”，直接将第i-1个区间加入结果
    # 如果第i个区间的起点比第i-1个区间的终点小，说明可以合并，那么将第i个和第i-1个区间合并，保存在第i个区间位置
    # 遍历结束后把最后一个区间加入结果
    
    res = []
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] > intervals[i-1][1]:
            res.append(intervals[i-1])
        else:
            new_start = min(intervals[i][0], intervals[i-1][0])
            new_end = max(intervals[i][1], intervals[i-1][1])
            intervals[i] = [new_start, new_end]
    
    res.append(intervals[-1])
    
    return res