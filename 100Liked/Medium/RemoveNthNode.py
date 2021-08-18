def removeNode(head, n):
    # 原始方法，部分是对的
    slow = None
    ori = fast = head
    k = 0
    while head:

        if k > n:
            slow = fast
            fast = fast.next
        
        k += 1
        head = head.next
    
    slow.next = fast.next

    return ori

def removeNode2(head, n):
    slow = fast = head
    for _ in range(n):
        # 使fast达到第n个节点
        fast = fast.next
    if not fast:
        # 长度不够，直接返回None
        return head.next
    
    while fast.next:
        # 遍历完之后，fast在结尾，slow在倒数第n个
        # 这里还是双指针法
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next

    return head