class Solution:

  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # # HASHMAP
    # hashmap = {}

    # for s in strs:
    #   # 1. Sort characters in string s.
    #   # Example: "eat" -> ['a', 'e', 't']
    #   s_sorted = sorted(s)

    #   # 2. Convert list to a tuple because lists are mutable and cannot be hashmap keys,
    #   # but tuples are immutable and valid dictionary keys.
    #   key = tuple(s_sorted)

    #   # 3. Add to hashmap under the common anagram key
    #   if key not in hashmap:
    #     hashmap[key] = [s]  # First string found for this anagram pattern
    #   else:
    #     hashmap[key].append(s)  # Append string to existing anagram group

    # # 4. Convert dict_values view object into a standard Python list
    # return list(hashmap.values())


    # MORE EFFICIENT (TOUGH TO UNDERSTAND)
    res = defaultdict(list)

    for string in strs:
        count = [0] * 26 # a ... z Frequency array for letters 'a' through 'z'

        # 1. Count ALL characters for the word FIRST
        for char in string:
            count[ord(char) - ord("a")] += 1 # EX. a = 80, a -> 80 - 80 = 0
                                        # and b = 81, b -> 81 - 80 = 1
        # 2. Append string to dictionary AFTER building full character count signature                                        
        res[tuple(count)].append(string)
        
    
    return list(res.values())

