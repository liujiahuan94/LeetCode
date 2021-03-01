def valid_parenthes(par):
    """
    :type par: list[str]
    :rtype: bool
    """
    left = '([{'
    par_dict = {')': '(', ']': '[', '}': '{'}
    # stack = [par[0]]
    stack = []

    if len(par) % 2 != 0:
        return False

    for i in range(0, len(par)):
        if par[i] in left:
            stack.append(par[i])
        else:
            if stack:
                if par_dict[par[i]] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                return False

    return not stack



if __name__ == '__main__':
    par = '()}{'
    re = valid_parenthes(par)
    print(re)

