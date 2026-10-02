class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            s_sorted = sorted(s)
            key = tuple(s_sorted)

            if key not in hashmap:
                hashmap[key] = [s]
            else:
                hashmap[key].append(s)
        
        return list(hashmap.values())