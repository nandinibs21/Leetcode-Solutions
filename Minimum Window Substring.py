class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        need = Counter(t)
        required = len(need)

        have = {}
        formed = 0

        left = 0
        min_len = float('inf')
        min_window = (0, 0)

        for right, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] == need[ch]:
                formed += 1

            # Try contracting while window is valid
            while formed == required:
                # Update best window
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_window = (left, right + 1)

                # Pop from left
                left_ch = s[left]
                have[left_ch] -= 1
                if left_ch in need and have[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

        if min_len == float('inf'):
            return ""
        start, end = min_window
        return s[start:end]
