class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        
        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            
            # Base case
            if a == b:
                memo[(a, b)] = True
                return True
            
            # Prune via char counts
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False
            
            n = len(a)
            
            # Try all possible splits
            for i in range(1, n):
                # no swap case
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                # swap case
                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True
            
            memo[(a, b)] = False
            return False
        
        return dfs(s1, s2)
