class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        longest = 0
        maxChar = [0] * 26

        for right in range(n):
            maxChar[ord(s[right]) - 65] += 1
            
            

            while (right - left) + 1 - max(maxChar) > k:
                maxChar[ord(s[left]) - 65] -= 1
                left += 1
            
            longest = max(longest, (right - left) + 1)
        
        return longest