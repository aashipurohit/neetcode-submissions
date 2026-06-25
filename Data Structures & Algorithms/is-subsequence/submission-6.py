class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sum_ = 0
        k = 0
        i,j = 0,0
        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                sum_ += 1
                i += 1
                j += 1
            else:
                i += 1
            
           
        return len(s) == sum_


        