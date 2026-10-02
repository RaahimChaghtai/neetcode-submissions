from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # HASHMAP AND SORTING TIME: O(nlogn) 
        # # 1. Count frequencies using a hash map
        # res = {}
        # for n in nums:
        #     res[n] = 1 + res.get(n, 0)

        # # 2. Store (frequency, key) pairs so sorting uses frequency and sort in descending order
        # ans = []
        # for key, value in res.items():
        #     ans.append((value, key))
    
        # ans.sort(reverse=True)
        
        # # 4. Extract the top k numbers
        # result = []
        # for i in range(k):
        #     result.append(ans[i][1]) # ans[i][1] gets the actual number
        
        # return result

        # BUCKET SORT (MORE EFFICIENT BUT HARD) TIME: O(n)
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n + 1) # [1, 2, 3] -> [0, 0, 0, 0]

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ret = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        return ret

        