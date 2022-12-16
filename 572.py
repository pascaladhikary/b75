class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        notes:  need two recursions, when node = subRoot.val, recurse in parallel
        '''
        s = subRoot
        
        def isEqual(n, s):
            if not n and not s:
                return True
            if n and s:
                return n.val == s.val and isEqual(n.left, s.left) and isEqual(n.right, s.right)
            return False
                       
        def dfs(n):
            if n == None:
                return False
            if n.val == s.val and isEqual(n, s):
                return True
            return dfs(n.left) or dfs(n.right)
        
        return dfs(root)