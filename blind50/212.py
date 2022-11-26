class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
    def addWord(self, word):
        s = self
        for c in word:
            if c not in s.children:
                s.children[c] = TrieNode()
            s = s.children[c]
        s.end = True
        
class Solution:
    '''
    notes:  trie, dfs works but is slow
    crux:   TLE unless you del node/prune word
    '''
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        r, c = len(board), len(board[0])
        res, seen = set(), set()
        
        trie = TrieNode()
        for w in words:
            trie.addWord(w)
            
        def dfs(i, j, node, word):
            if (i, j) in seen or board[i][j] not in node.children:
                return
                
            seen.add((i, j))
            word += board[i][j]
            node = node.children[board[i][j]]
            
            if node.end: 
                res.add(word)
            
            if not node.children:
                del node
            else:
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for y, x in directions:
                    if -1 < i+y < r and -1 < j+x < c: 
                        dfs(i+y, j+x, node, word)      
                        
            seen.remove((i, j))
            
        for i in range(r):
            for j in range(c):
                dfs(i, j, trie, '')
                
        return res