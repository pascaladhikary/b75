class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        notes:  swap children
        crux:   account for uneven leaves
        '''
        def invert(node):
            if node == None:
                return
            
            node.left, node.right = invert(node.right), invert(node.left)            
            return node
        
        return invert(root)