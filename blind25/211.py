class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class WordDictionary:
    '''
    notes:  implement trie
    crux:   dfs but need to pass in i
    '''

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        n = self.root
        
        for c in word:
            if c not in n.children:
                n.children[c] = TrieNode()
            n = n.children[c]  
        n.end = True

    def search(self, word: str) -> bool:
        n = self.root
        
        def helper(n, i):
            if i == len(word):
                return n.end
            c = word[i]
            
            if c == ".":
                for ch in n.children.values():
                    if helper(ch, i+1): return True  
                return False
                    
            if c in n.children:
                return helper(n.children[c], i+1)
            return False
        
        return helper(n, 0)