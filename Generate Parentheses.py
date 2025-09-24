from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr: str, open_count: int, close_count: int):
            # If both counts reach n, we've formed a valid combo
            if open_count == n and close_count == n:
                res.append(curr)
                return

            # Add '(' if possible
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Add ')' if valid
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res
