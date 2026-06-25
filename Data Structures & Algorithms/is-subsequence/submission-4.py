class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sum = 0
        k = 0
        for i in range(len(s)):
            for j in range(k,len(t)):
                if s[i] == t[j]:
                    sum += 1
                    k = j+1
                    break
        return len(s) == sum


        