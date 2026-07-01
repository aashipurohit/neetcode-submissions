class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0 
        left = 0
        for i in range(len(nums)):
            sum += nums[i]
        for j in range(len(nums)):
            right = sum - left - nums[j]
            if left == right:
                return j
            left += nums[j] 
        return -1


        