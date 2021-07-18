def addTwoNumber(l1, l2):
    '''
    基本思想是，两个数相加，然后考虑进位carry
    遍历两个链表，然后取值，把两个值(如果有的话)和进位一起相加
    然后把相加结果除以10并取10的余数，商是进位，余数是当前节点的值
    '''
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next



