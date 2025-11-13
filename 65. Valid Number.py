class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        num_seen = False
        dot_seen = False
        e_seen = False
        num_after_e = True

        for i, c in enumerate(s):
            if c.isdigit():
                num_seen = True
                if e_seen:
                    num_after_e = True

            elif c in ['+', '-']:
                # sign only allowed at start or right after e/E
                if i > 0 and s[i-1].lower() not in ['e']:
                    return False

            elif c == '.':
                # dot not allowed after dot or exponent
                if dot_seen or e_seen:
                    return False
                dot_seen = True

            elif c.lower() == 'e':
                # e only allowed once, only after a number
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_after_e = False  # must get digits after e

            else:
                return False

        return num_seen and num_after_e
