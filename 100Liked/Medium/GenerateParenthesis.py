def generateParenthesis(n):
    results = []

    def helper(so_far, results, left, right):
        if left == 0 and right == 0:
            results.append(so_far)
        
        if left > 0:
            helper(so_far+'(', results, left-1, right)
        
        if right > left:
            helper(so_far+')', results, left, right-1)
        
    helper('', results, n, n)

    return results


if __name__ == '__main__':
    re = generateParenthesis(3)
    print(re)

