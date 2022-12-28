class Codec:

    def serialize(self, root):
        '''
        notes:  preorder traversal
        crux:   need array for negatives
        '''
        res = []
        
        def preorder(node):
            if node == None:
                res.append('null')
                return
                
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        return (',').join(res)

    def deserialize(self, data):
        '''
        notes:  undo-ing preorder recursively
        crux:   global variable i
        '''
        d = data.split(',')
        
        self.i = 0
        def preorder():
            if d[self.i] == 'null':
                self.i += 1
                return None
            
            node = TreeNode(d[self.i])
            self.i += 1 

            node.left = preorder()
            node.right = preorder()    

            return node
        
        return preorder()