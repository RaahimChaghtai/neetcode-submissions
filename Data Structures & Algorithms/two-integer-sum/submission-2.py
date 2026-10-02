class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # HASHMAP
        # Store numbers we have already seen.
        # The key is the number itself, and the value is its index.
        prevMap = {}

        # Go through the array from left to right.
        for i, n in enumerate(nums):
            # Calculate the number needed to add to the current number
            # in order to reach the target.
            diff = target - n

            # If the needed number was seen earlier, we found the pair.
            # prevMap[diff] gives the earlier number's index.
            # Since we scan from left to right, that index is smaller than i.
            if diff in prevMap:
                return [prevMap[diff], i]

            # We have not found a pair with n yet, so save its index
            # for future numbers to use as their complement.
            prevMap[n] = i

        # The problem guarantees that a valid pair always exists,
        # so this line should never be reached.
        return []