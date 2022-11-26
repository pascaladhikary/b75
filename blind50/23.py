class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        notes:  iterate, merge two lists at a time until 1 list remains
        crux:   set dummy to reference of head
        '''
        def mergeLists(l1, l2):
            dummy = ListNode()
            tail = dummy
            
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next   
                
            tail.next = l2 if l2 else l1
            return dummy.next
        
        if not lists: return None
        
        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 != len(lists) else None
                merged.append(mergeLists(l1, l2))

            lists = merged
            
        return lists[0]