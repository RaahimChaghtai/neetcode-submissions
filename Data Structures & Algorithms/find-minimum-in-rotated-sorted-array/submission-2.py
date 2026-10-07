class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## O(n) 
        #min_num = float('inf')
        #for num in nums:
        #    if num < min_num:
        #        min_num = num
        
        #return min_num

        # O(log n)
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]


        