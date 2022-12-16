class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        notes:  backtracking
        crux:   TLE requires a few optimizations
                set # instead of seen set
                check if word can be constructed
                reverse word if first letter occurs more than last letter of the word
        '''
        r, c = len(board), len(board[0])
        
        def dfs(i, j, k):
            if k == len(word):
                return True
            if not (-1 < i < r and -1 < j < c) or board[i][j] != word[k]:
                return
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            res = False
            
            temp = board[i][j]
            board[i][j] = "#"
            
            for y,x in directions:
                if dfs(i+y, j+x, k+1):
                    res = True
                    break
                        
            board[i][j] = temp
            return res
        
        chars = [c for row in board for c in row]
        word_count = collections.Counter(word)
        board_count = collections.Counter(chars)

        for char, count in word_count.items():
            if count > board_count[char]: return False

        if board_count[word[0]] > board_count[word[-1]]: word = word[::-1]
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0): return True