from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        counter = Counter()

        # Count bulls and store unmatched secret digits
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                counter[s] += 1

        cows = 0

        # Count cows
        for s, g in zip(secret, guess):
            if s != g and counter[g] > 0:
                cows += 1
                counter[g] -= 1

        return f"{bulls}A{cows}B"
