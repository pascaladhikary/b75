class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        notes:  create graph c: set()
                it is a DAG, think like tree a->b->c and a->c
                instead of finding root a, just dfs bottom up and 
                use seen to mark both cycle and visited
        crux:   DAG
        '''
        graph = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[c1].add(c2)
                    break
        
        seen = {}
        res = collections.deque()

        def dfs(c):
            if c in seen:
                return seen[c]

            seen[c] = True
            for n in graph[c]:
                if dfs(n):
                    return True
            seen[c] = False
            res.appendleft(c)

        for c in graph:
            if dfs(c): return ""

        return "".join(res)