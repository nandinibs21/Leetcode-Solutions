from typing import List, Dict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)

        # DP prune: can[i] = whether s[i:] can be segmented
        can = [False] * (n + 1)
        can[n] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if s[i:j] in word_set and can[j]:
                    can[i] = True
                    break

        if not can[0]:
            return []

        memo: Dict[int, List[str]] = {}

        def dfs(i: int) -> List[str]:
            if i in memo:
                return memo[i]
            if i == n:
                return [""]  # sentinel: one valid way to finish

            res: List[str] = []
            # Only explore if remainder is segmentable
            for j in range(i + 1, n + 1):
                if not can[j]:
                    continue
                w = s[i:j]
                if w in word_set:
                    for tail in dfs(j):
                        res.append(w if tail == "" else w + " " + tail)

            memo[i] = res
            return res

        return dfs(0)
