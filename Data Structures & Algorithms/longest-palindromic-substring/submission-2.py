class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_len = 0

        for i in range(len(s)):
            # ODD length
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Check if this is the LONGEST substring
                if (right - left + 1) > res_len:
                    res = s[left:right + 1] 
                    res_len = (right - left + 1)
                left -= 1
                right += 1
            
            # EVEN length
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Check if this is the LONGEST substring
                if (right - left + 1) > res_len:
                    res = s[left:right + 1] 
                    res_len = (right - left + 1)
                left -= 1
                right += 1
        return res



        # n = len(s)
        # if n <= 1:
        #     return s

        # # Create a 2D table of size n x n filled with False
        # # (Using standard loops instead of list comprehensions)
        # dp = []
        # for i in range(n):
        #     row = []
        #     for j in range(n):
        #         row.append(False)
        #     dp.append(row)
        
        # start = 0
        # max_len = 0

        # # Base case 1: Every single character is a palindrome of length 1
        # for i in range(n):
        #     dp[i][i] = True
        #     max_len = 1
        #     start = i

        # # Base case 2: Check all substrings of length 2
        # for i in range(n - 1):
        #     if s[i] == s[i + 1]:
        #         dp[i][i + 1] = True
        #         start = i
        #         max_len = 2

        # # Check lengths 3 and greater
        # for length in range(3, n + 1):
        #     for i in range(n - length + 1):
        #         j = i + length - 1 # End index
                
        #         # State transition: outer chars match AND inner substring is a palindrome
        #         if s[i] == s[j] and dp[i + 1][j - 1]:
        #             dp[i][j] = True
        #             if length > max_len:
        #                 max_len = length
        #                 start = i

        # return s[start : start + max_len]