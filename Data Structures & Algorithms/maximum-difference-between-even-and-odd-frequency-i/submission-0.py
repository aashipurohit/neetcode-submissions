class Solution:
    def maxDifference(self, s: str) -> int:
        result = {}
        for i in s:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        
        x = list(result.values())
        odd_freq = []
        even_freq = []
        for j in x:
            if j%2!=0:
                odd_freq.append(j)
            else:
                even_freq.append(j)
        a1 = max(odd_freq)
        a2 = min(even_freq)
        return a1 - a2
     
                




        