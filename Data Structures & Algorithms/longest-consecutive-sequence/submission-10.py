class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        z = 1
        m = set(nums)
        y = list(m)
        y.sort()
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        for i in range(len(y)-1):
            if y[i] == y[i+1] - 1:
                count += 1
                z = max(count,z)
            elif count >= 1:
                count = 1
        return z
        
        