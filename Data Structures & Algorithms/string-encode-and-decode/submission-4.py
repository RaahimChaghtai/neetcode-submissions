class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Takes a list of strings and packs them into a single encoded string.
        Strategy: [Length] + [#] + [Actual String]
        Example: ["hello", "world"] -> "5#hello5#world"
        """
        res = ""
        for s in strs:
            # Append the length of the string, a '#' separator, and the string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """
        Takes the single encoded string and unpacks it back into the original list of strings.
        Strategy: Use a pointer 'i' to scan through the string, find the '#', read the 
        length before it, and slice out the exact number of characters that follow.
        """
        res = []
        i = 0  # Pointer to track our current position in the encoded string
        
        while i < len(s):
            j = i
            
            # Step 1: Find where the '#' delimiter is located.
            # Everything between 'i' and 'j' represents the length of the upcoming word.
            while s[j] != "#":
                j += 1
            
            # Step 2: Extract the length substring and convert it to an integer.
            length = int(s[i:j])
            
            # Step 3: Extract the actual string using the length we just found.
            # The word starts right after '#' (which is at index j + 1) 
            # and spans for 'length' characters.
            word_start = j + 1
            word_end = word_start + length
            res.append(s[word_start:word_end])
            
            # Step 4: Jump pointer 'i' past the current word so we can process the next encoded item.
            i = word_end
        
        return res