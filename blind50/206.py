class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        notes:  rev starting at 0
        '''
        
        c, p, n = head, None, None
        
        while c != None:
            n = c.next 
            c.next = p
            p = c
            c = n
            
        return p
        