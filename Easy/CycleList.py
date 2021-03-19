def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False