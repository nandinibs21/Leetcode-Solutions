class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        m, n = len(board), len(board[0])
        word_len = len(word)
        
        # Optional pruning: if word has a character more times than the board does,
        # we can immediately return False.
        from collections import Counter
        
        board_counter = Counter()
        for r in range(m):
            for c in range(n):
                board_counter[board[r][c]] += 1
        
        word_counter = Counter(word)
        for ch, cnt in word_counter.items():
            if board_counter[ch] < cnt:
                return False  # impossible to form word
        
        def dfs(r: int, c: int, i: int) -> bool:
            """
            Return True if we can form word[i:] starting from board[r][c].
            """
            # If current char doesn't match, fail
            if board[r][c] != word[i]:
                return False
            
            # If we've matched the last character, success
            if i == word_len - 1:
                return True
            
            # Mark as visited by temporarily changing the value
            temp = board[r][c]
            board[r][c] = "#"  # any sentinel that isn't a valid letter
            
            # Explore neighbors
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                    if dfs(nr, nc, i + 1):
                        # Restore before returning
                        board[r][c] = temp
                        return True
            
            # Restore on backtrack
            board[r][c] = temp
            return False
        
        # Try each cell as a starting point
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False
