from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        k = len(words[0])
        m = len(words)
        total = m * k
        n = len(s)

        target = Counter(words)
        result = []

        # Check each possible offset
        for offset in range(k):
            left = offset
            window_count = Counter()
            count = 0  # number of valid words matched

            # Move the right pointer in steps of k
            for right in range(offset, n - k + 1, k):
                word = s[right:right + k]

                if word in target:
                    window_count[word] += 1
                    count += 1

                    # Too many copies? shrink window
                    while window_count[word] > target[word]:
                        left_word = s[left:left + k]
                        window_count[left_word] -= 1
                        left += k
                        count -= 1

                    # Perfect window size?
                    if count == m:
                        result.append(left)
                else:
                    # reset everything
                    window_count.clear()
                    count = 0
                    left = right + k

        return result
