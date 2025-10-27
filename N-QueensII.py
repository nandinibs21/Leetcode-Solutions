class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        cols = set()
        pos_diag = set()  # r + c
        neg_diag = set()  # r - c

        def backtrack(r):
            if r == n:
                self.count += 1
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # place queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack(r + 1)

                # backtrack
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)
        return self.count
