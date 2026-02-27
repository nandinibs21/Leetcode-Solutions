from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        ans = 1

        for i in range(n):
            slopes = defaultdict(int)
            same = 0  # duplicates of points[i], should be 0 given constraints
            best = 0

            xi, yi = points[i]

            for j in range(i + 1, n):
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi

                if dx == 0 and dy == 0:
                    same += 1
                    continue

                # Normalize vertical/horizontal and general slope as reduced pair (dy, dx)
                if dx == 0:
                    key = (1, 0)          # vertical
                elif dy == 0:
                    key = (0, 1)          # horizontal
                else:
                    g = gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g

                    # Normalize sign: keep dx positive
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    key = (dy, dx)

                slopes[key] += 1
                best = max(best, slopes[key])

            # +1 for the anchor point itself, +same for duplicates (if any)
            ans = max(ans, best + same + 1)

        return ans
