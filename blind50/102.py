class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        notes:  bfs
        '''
        if not root: return None
        res, level = [], [root]
        
        while level:
            res.append([n.val for n in level])
            next_level = []
            
            for n in level:
                if n.left: 
                    next_level.append(n.left)
                if n.right: 
                    next_level.append(n.right)
            
            level = next_level        
        return res