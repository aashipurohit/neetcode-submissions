class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seen2 = {}
        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for i in t:
            if i in seen2:
                seen2[i] += 1
            else:
                seen2[i] = 1
        
        if seen == seen2:
            return True
        return False
        
        