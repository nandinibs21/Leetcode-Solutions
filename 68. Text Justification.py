class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0

        while i < len(words):
            line_len = len(words[i])
            j = i + 1

            # Greedily pack words
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            # Build the line
            line_words = words[i:j]
            gaps = j - i - 1

            # Last line or single-word line → left-justify
            if j == len(words) or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                res.append(line)
            else:
                total_chars = sum(len(w) for w in line_words)
                total_spaces = maxWidth - total_chars

                space_each = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    # Left slots get the extra spaces
                    line += " " * (space_each + (1 if k < extra else 0))
                line += line_words[-1]

                res.append(line)

            i = j

        return res
