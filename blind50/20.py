class Solution:
    def isValid(self, s: str) -> bool:
        '''
        notes:  stack
        '''
        stack = []
        p = {'(': ')', '{': '}', '[': ']'}
        
        if len(s) < 2: 
            return False
        
        for c in s:
            if c in p.keys():
                stack.append(c)
            elif len(stack) == 0 or p[stack.pop()] != c:
                return False
                
        return len(stack) == 0