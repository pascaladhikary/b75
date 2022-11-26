class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        notes:  seen set
        '''
        seen = set()
        c = head
        
        while c != None:
            if c in seen:
                return True
            seen.add(c)
            c = c.next
        
        return False