class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i , num in enumerate(nums):
            diff = target - nums[i]
            if diff in res:
                return [res[diff]+1,i+1]
            res[num] = i
        return -1
        
        
        