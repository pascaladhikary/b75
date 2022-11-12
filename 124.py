class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        notes:  dfs (bottom up)
        crux:   max(n, 0) for negatives
                l, r, or l+r but a join is always 
                checked since a neg will be set to 0 
        '''
        self.res = root.val
        
        def pathSum(node):
            if node == None:
                return 0
            
            l = max(pathSum(node.left), 0)
            r = max(pathSum(node.right), 0)
            self.res = max(self.res, l + r + node.val)
            
            return node.val + max(l, r)
        
        pathSum(root)
        return self.res