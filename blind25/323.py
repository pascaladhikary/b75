class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> bool:
        '''
        notes:  dfs
        '''
        k = n
        graph = collections.defaultdict(set)
        
        for (n, c) in edges:
            graph[n].add(c)
            graph[c].add(n)

        seen = set()
        def dfs(c, p):
            if c not in graph:
                return
            if c in seen:
                return True

            seen.add(c)
            for n in graph[c]:
                if n == p:
                    continue
                if dfs(n, c):
                    return True
            
        count = 0
        for c in graph:
            if not dfs(c, -1): count += 1

        return count