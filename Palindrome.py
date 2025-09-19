class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check if an integer x is a palindrome.

        Steps:
        1. Convert the integer to a string.
        2. Reverse the string.
        3. Compare original string with reversed string.
        4. Return True if they are equal, else False.
        """
        # Step 1: Convert the integer to string
        original_str = str(x)

        # Step 2: Reverse the string
        reversed_str = original_str[::-1]

        # Step 3: Compare original and reversed strings
        return original_str == reversed_str

# Local testing (not needed on LeetCode)
if __name__ == "__main__":
    sol = Solution()

    test_cases = [121, -121, 10, 0, 12321, 12345]
    for x in test_cases:
        print(f"isPalindrome({x}) = {sol.isPalindrome(x)}")
