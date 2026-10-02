class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # HASHMAP
        # prevMap = {}

        # for i, n in enumerate(numbers):
        #     diff = target - n 

        #     if diff in prevMap:
        #         return [prevMap[diff] + 1, i + 1]
            
        #     prevMap[n] = i
        
        # return 

        # 2 POINTERS
        n = len(numbers)
        left = 0
        right = n - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [left + 1, right + 1]
            
            elif currentSum > target:
                right -= 1
            else:
                left += 1
        return []