from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        L = len(beginWord)
        parents = defaultdict(list)   # child -> [parents...]
        dist = {beginWord: 0}

        q = deque([beginWord])
        found_end = False
        level = 0

        while q and not found_end:
            level_size = len(q)
            level += 1

            # We want to ensure we only set "newly discovered" nodes for this level once,
            # but still allow multiple parents from the same level.
            this_level_seen = set()

            for _ in range(level_size):
                cur = q.popleft()
                cur_list = list(cur)

                for i in range(L):
                    original = cur_list[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == original:
                            continue
                        cur_list[i] = c
                        nxt = "".join(cur_list)

                        if nxt in wordSet:
                            # First time ever discovered => shortest
                            if nxt not in dist:
                                dist[nxt] = level
                                parents[nxt].append(cur)
                                if nxt not in this_level_seen:
                                    q.append(nxt)
                                    this_level_seen.add(nxt)
                                if nxt == endWord:
                                    found_end = True
                            # Already discovered at same shortest level => add another parent
                            elif dist[nxt] == level:
                                parents[nxt].append(cur)

                    cur_list[i] = original

        if endWord not in dist:
            return []

        res = []
        path = [endWord]

        def dfs(word: str):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)
        return res
