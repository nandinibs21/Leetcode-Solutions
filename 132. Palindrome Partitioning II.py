from typing import List

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0

        # dp[i] = min cuts needed for s[:i] (first i chars)
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = i - 1  # worst case: cut between every char

        # Expand around centers to find palindromes and relax dp
        for center in range(n):
            # Odd-length palindromes
            l, r = center, center
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1

            # Even-length palindromes
            l, r = center, center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1

        return dp[n]
