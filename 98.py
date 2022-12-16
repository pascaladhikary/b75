class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        notes:  just replacing bound w/ previous node value
        crux:   left & right are bounds
        '''
        def isValid(l, node, r):
            if node == None:
                return True
            if not l < node.val < r:
                return False
            return isValid(l, node.left, node.val) and isValid(node.val, node.right, r)
            
        return isValid(float(-inf), root, float(inf))