class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        notes:  two ptr
        crux:   we only need to contract at lower height
        '''
        w = -1
        l, r = 0, len(height)-1
        
        while l != r:
            w = max(w, (r-l) * min(height[l], height[r]))
            
            if height[l] <= height[r]:
                l +=1
            else:
                r -= 1 
                
        return w