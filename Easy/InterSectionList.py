def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    # 把一个链表与两一个连起来，然后遍历，如果有相交，一定会有相等的地方
    # A=[1, 2, 3, 6, 7, 8]
    # B=[5, 6, 7, 8]
    # 连起来
    # (1) 1 2 3 6 7 8 N 5 6
    # (2) 5 6 7 8 N 1 2 3 6
    n1, n2 = headA, headB
    while n1 != n2:
        n1 = n1.next if n1 else headB
        n2 = n2.next if n2 else headA
    
    return n1