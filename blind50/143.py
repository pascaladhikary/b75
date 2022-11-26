class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        notes:  find middle, reverse latter, merge
        '''
        if not head or not head.next: return head
        
        c, f = head, head
        while f and f.next:
            c = c.next
            f = f.next.next
        
        temp = c.next
        c.next = p = None
        c = temp
        
        while c:
            temp = c.next
            c.next = p
            p = c
            c = temp
            
        l1, l2 = head, p
        while l1 and l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2