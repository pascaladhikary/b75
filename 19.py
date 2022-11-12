class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        notes:  move r to n, then move both
                dummy puts l behind remove node
        '''
        
        dummy = ListNode(0, head)
        l, r = dummy, head
        
        c = 0
        while c < n:# and r != None:
            r = r.next
            c += 1
                    
        while r != None:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        return dummy.next