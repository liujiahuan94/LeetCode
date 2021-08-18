# 这是一个类似于斐波那契数列的问题，第n级台阶的上法等于第n-1和n-2级之和
#1 递归加字典记忆，avoid repeating computation
def __init__(self):
    self.dic = {1:1, 2:2}
    
def climbStairs1(self, n):
    if n not in self.dic:
        self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
    return self.dic[n]

# 递归
# Bottom up, O(n) space
def climbStairs2(self, n):
    if n == 1:
        return 1
    res = [0 for i in range(n)]
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[-1]
