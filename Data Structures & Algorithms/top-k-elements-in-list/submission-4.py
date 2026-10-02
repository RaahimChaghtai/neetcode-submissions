from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HASHMAP AND SORTING - TIME: O(nlogn) 
        # 1. Count frequencies using a hash map
        res = {}
        for n in nums:
            res[n] = 1 + res.get(n, 0)

        # 2. Store (frequency, key) pairs so sorting uses frequency and sort in descending order
        ans = []
        for key, value in res.items():
            ans.append((value, key))
    
        ans.sort(reverse=True)
        
        # 4. Extract the top k numbers
        result = []
        for i in range(k):
            result.append(ans[i][1]) # ans[i][1] gets the actual number
        
        return result

        # # BUCKET SORT (MORE EFFICIENT BUT HARD) - TIME: O(n)
        # n = len(nums)

        # # 1. COUNT FREQUENCIES
        # # Counter creates a dictionary mapping number -> count.
        # # Example: [1, 1, 1, 2, 2, 3] -> {1: 3, 2: 2, 3: 1}
        # counter = Counter(nums)

        # # 2. INITIALIZE BUCKETS
        # # Size is (n + 1) because the highest possible frequency of an element is `n`.
        # # We use 0 as a placeholder to indicate an empty bucket.
        # buckets = [0] * (n + 1) # [1, 2, 3] -> [0, 0, 0, 0]

        # # 3. GROUP NUMBERS BY THEIR FREQUENCY
        # # Loop over every unique (number, frequency) pair.
        # for num, freq in counter.items():

        #     # If no number has had this frequency yet, create a new list for it.
        #     if buckets[freq] == 0:
        #         buckets[freq] = [num]
            
        #     # If a list already exists at this frequency index, append the number to it.
        #     else:
        #         buckets[freq].append(num)
        
        # # 4. GATHER TOP K FREQUENT ELEMENTS
        # ret = []

        # # Iterate backwards from index `n` down to `0` (highest frequency to lowest frequency).
        # for i in range(n, -1, -1):

        #     # Skip empty buckets
        #     if buckets[i] != 0:
        #         # Add all numbers that appeared `i` times into our result list.
        #         ret.extend(buckets[i])

        #     # Stop collecting once we have gathered `k` elements.
        #     if len(ret) == k:
        #         break

        # return ret

        