class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        x = sorted(count.items(), key = lambda p:p[1], reverse = True)
        z = []
        for i in range(k):
           z.append(x[i][0])
        return z
        
        