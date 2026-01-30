from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        L = len(beginWord)

        # pattern -> words
        buckets = defaultdict(list)
        for w in wordSet:
            for i in range(L):
                buckets[w[:i] + "*" + w[i+1:]].append(w)

        q = deque([(beginWord, 1)])  # (word, distance in words)
        visited = set([beginWord])

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist

            for i in range(L):
                pat = word[:i] + "*" + word[i+1:]
                for nxt in buckets[pat]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, dist + 1))
                buckets[pat].clear()  # important prune

        return 0
from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        L = len(beginWord)

        # pattern -> words
        buckets = defaultdict(list)
        for w in wordSet:
            for i in range(L):
                buckets[w[:i] + "*" + w[i+1:]].append(w)

        q = deque([(beginWord, 1)])  # (word, distance in words)
        visited = set([beginWord])

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist

            for i in range(L):
                pat = word[:i] + "*" + word[i+1:]
                for nxt in buckets[pat]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, dist + 1))
                buckets[pat].clear()  # important prune

        return 0
