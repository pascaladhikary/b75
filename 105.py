class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        notes:  preorder = [3,9,20,15,7]
                inorder = [9,3,15,20,7]
                we know 3 is root, left before, right after
                [9], [20, 15, 7]
                recurse with preorder: [9,20,15,7]
                base case when i is None
        
        crux:   first elem of preorder is root
                root splits inorder left : root : right
        '''
        def build(p, i):
            if not i:
                return None
            pos = i.index(p.pop(0))
            node = TreeNode(i[pos])
            node.left, node.right = build(p, i[:pos]), build(p, i[pos+1:])
            return node
            
        return build(preorder, inorder)