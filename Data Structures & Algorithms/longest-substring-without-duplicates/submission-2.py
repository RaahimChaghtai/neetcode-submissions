class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # Stores unique characters in the current window
        left = 0         # Left boundary of the sliding window
        longest = 0      # Tracks the maximum substring length found
        n = len(s)

        for right in range(n):
            # If s[right] is already in our window, shrink the window from the left
            # until s[right] is no longer a duplicate inside the set.
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1  # Move left pointer forward to shrink window
            
            # Add current character to set (it is now safe since duplicates were removed)
            charSet.add(s[right])

            # Length of current valid window is (right - left + 1)
            window = (right - left) + 1

            # Update maximum length found so far
            longest = max(longest, window)
        
        return longest