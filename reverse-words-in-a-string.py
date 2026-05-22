class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split()

        # Reverse the list of words
        words.reverse()

        # Join words with a single space
        return " ".join(words)


# Example usage
sol = Solution()

print(sol.reverseWords("the sky is blue"))     
# Output: "blue is sky the"

print(sol.reverseWords("  hello world  "))    
# Output: "world hello"

print(sol.reverseWords("a good   example"))   
# Output: "example good a"
