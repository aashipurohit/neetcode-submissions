class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        oddmax , evenmin = 0 , len(s)
        for i in count.values():
            if i & 1:
                oddmax = max(oddmax,i)
            else:
                evenmin = min(evenmin,i)
        
        return oddmax - evenmin