class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        notes:  dfs, hold prev as bidirectional
        crux:   we know we can start a 0, no need to backtrack
        '''
        k = n
        graph = collections.defaultdict(set)
        if not edges and n == 1: return True
        
        for (n, c) in edges:
            graph[n].add(c)
            graph[c].add(n)

        seen = set()
        def dfs(c, prev):
            if c not in graph:
                return
            if c in seen:
                return True
            
            seen.add(c)
            for n in graph[c]:
                if n == prev:
                    continue
                if dfs(n, c):
                    return True
                
        return not dfs(0, -1) and len(seen) == k