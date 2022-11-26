class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        notes:  dfs
        crux:   from 1 dfs is on 2
                w/ neighbor 1, 3 and 1 has been seen
                so append seen[n] to avoid cycle
        '''
        seen = {}
        def dfs(node):
            if node in seen:
                return seen[node]
            
            node_copy = Node(node.val)
            seen[node] = node_copy
            
            for n in node.neighbors:
                node_copy.neighbors.append(dfs(n))
                    
            return node_copy
        
        return None if not node else dfs(node)