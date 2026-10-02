class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        longest = 0
        n = len(s)

        for right in range(n):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            window = (right - left) + 1

            longest = max(longest, window)
            
            charSet.add(s[right])
        
        return longest