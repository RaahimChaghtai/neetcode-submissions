class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {")": "(", 
                   "}": "{",
                   "]": "["}

        for char in s:
            if char in mapping:
                closing_bracket = mapping[char]
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = 1

                if closing_bracket != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack