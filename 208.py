class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class Trie:
    '''
    notes:  use hashmap for easier lookup
            first TrieNode technically holds all roots
    crux:   need end flag bc app/apple
    '''

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        n = self.root

        for c in word:
            if c not in n.children:
                n.children[c] = TrieNode()
            n = n.children[c]
        n.is_end = True

    def search(self, word: str) -> bool:
        n = self.root

        for c in word:
            if c not in n.children: 
                return False
            n = n.children[c]

        return n.is_end

    def startsWith(self, prefix: str) -> bool:
        n = self.root

        for c in prefix:
            if c not in n.children: 
                return False
            n = n.children[c]

        return True