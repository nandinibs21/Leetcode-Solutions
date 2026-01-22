from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        # dp initialized as the last row (base case)
        dp = triangle[-1][:]  # O(n) where n = number of rows
        
        # Build from second-last row up to the top
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        
        return dp[0]
