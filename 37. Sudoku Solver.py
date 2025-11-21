class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # Tracking sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empties = []

        # Initialize the tracking structures
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)

        def backtrack(idx):
            # All empty cells filled
            if idx == len(empties):
                return True

            r, c = empties[idx]
            box_idx = (r // 3) * 3 + (c // 3)

            for ch in '123456789':
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_idx]:
                    # Place ch
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_idx].add(ch)

                    # Recurse to next empty cell
                    if backtrack(idx + 1):
                        return True

                    # Backtrack
                    board[r][c] = '.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_idx].remove(ch)

            # No valid digit for this cell
            return False

        backtrack(0)
