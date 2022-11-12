class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        notes:  create graph
                dfs
                break point: reqs[c] = []
        
        crux:   we can use a seen set because the only time we don't remove is
                when we cycle, thus that specific class always cycles
        '''
        freq = collections.defaultdict(list)
        
        for c, p in prerequisites:
            freq[c].append(p)
            
        seen = set()
        def dfs(c):
            if c in seen:
                return False
            
            seen.add(c)
            for p in freq[c]:
                if not dfs(p):
                    return False
                
            seen.remove(c)
            freq[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
                                            
        return True