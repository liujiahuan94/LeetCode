def removeNode(head, n):
    # ori
    slow = None
    fast = head
    k = 0
    while head:
        if k < n:
            continue
        else:
            slow = fast
            fast = fast.next
        
        k += 1
        head = head.next
    
    slow.next = fast.next

    return 