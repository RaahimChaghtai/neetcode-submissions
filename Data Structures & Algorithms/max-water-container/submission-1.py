class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        amt =  float('-inf')

        while left < right:
            width = right - left
            min_height = min(heights[left], heights[right])
            area = min_height * width
            if area > amt:
                amt = area
            
            if heights[left] == min_height:
                left += 1
            else:
                right -= 1
        
        return amt