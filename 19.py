class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        notes:  move r to n, then move both
                dummy puts l behind remove node
                by starting one before head
        '''
        
        dummy = ListNode(0, head)
        l, r = dummy, head
        
        for i in range(n):
            r = r.next
                    
        while r != None:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        return dummy.next