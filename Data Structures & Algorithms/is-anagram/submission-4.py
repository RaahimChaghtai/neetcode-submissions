class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        num1 = {}
        num2 = {}

        for i in s:
            num1[i] = 1 + num1.get(i, 0) 
        
        for i in t:
            num2[i] = 1 + num2.get(i, 0) 
        
        
        for key, value in num1.items():
            if num1[key] != num2.get(key, 0):
                return False
        return True