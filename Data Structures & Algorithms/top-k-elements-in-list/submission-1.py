class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = {}
        for n in nums:
            res[n] = 1 + res.get(n, 0)
        
        ans = []
        for key, value in res.items():
            ans.append((value, key))
        
        ans.sort(reverse=True)
        
        result = []
        for i in range(k):
            result.append(ans[i][1])
        
        return result

        