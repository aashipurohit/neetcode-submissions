class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        unique = set(nums)
        for i in unique:
            if (i-1) not in unique:
                length = 1
                while (i + length) in unique:
                    length += 1
                longest = max(longest,length)
        return longest

    
        
        