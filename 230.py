class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        notes:  inorder traversal
        '''
        res = []
        
        def inorder(node):
            if node == None:
                return None
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res[k-1]