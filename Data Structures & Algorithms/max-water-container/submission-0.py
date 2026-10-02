class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_vol = 0
        while l < r:
            curr_vol = min(heights[l], heights[r]) * (r - l)

            max_vol = max(curr_vol, max_vol)

            new_r = r-1
            new_l = l+1

            if heights[r] > heights[l]:
                l = new_l
            else:
                r = new_r
        
        return max_vol
        