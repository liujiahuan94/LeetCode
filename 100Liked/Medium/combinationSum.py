def combinationSum(candidates, target):
    # 还是经典的回溯问题，不过这里的不同是，数字可以重复使用，因此，递归的时候不能把数字排除
    # 这题的关键是避免重复解，采取的措施是，递归的时候候选数字为nums[i:]，这样既没有把当前数字排除
    # 同时还每次都向后寻找数字，不回头找就不会产生重复解，这个技巧是本题的关键
    res = []
    def backTrack(path, target, nums, res):
        if target == 0:
            res.append(path[:])
            return 
        
        if target < 0:
            return

        for i in range(len(nums)):
            backTrack(path+[nums[i]], target-nums[i], nums[i:], res)
    
    backTrack([], target, candidates, res)
    
    return res


if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    re = combinationSum(candidates, target)
    print(re)

        