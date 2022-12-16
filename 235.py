class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        notes:  if we split we know it to be LCA due to BST
        crux:   iterate because BST
        '''
        c = root
        while True:
            if p.val > c.val and q.val > c.val:
                c = c.right
            elif p.val < c.val and q.val < c.val:
                c = c.left
            else:
                return c