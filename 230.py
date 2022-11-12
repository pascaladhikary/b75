class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        notes:  inorder traversal 
        '''
        res = []
        
        def helper(node):
            if node == None:
                return None
            
            helper(node.left)
            res.append(node.val)
            helper(node.right)
            
        helper(root)
        return res[k-1]