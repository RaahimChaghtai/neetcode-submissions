class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        longest = 0
        max_freq = 0
        count = {}

        for right in range(n):
            count[s[right]] = count.get(s[right], 0) + 1
            
            max_freq = max(max_freq, count[s[right]])


            while (right - left) + 1 - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            longest = max(longest, (right - left) + 1)
        
        return longest