class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        zero_count = nums.count(0)
        if zero_count == 1:
            x = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    x *= nums[i]
            for i in range(len(nums)):
                if nums[i] != 0:
                    result.append(0)
                else:
                    result.append(x)


        if zero_count >= 2:
            i = 0
            while i < len(nums):
                result.append(0)
                i += 1
        if zero_count == 0:
            for i in nums:
                product *= i
            for i in range(len(nums)):
                x = product//nums[i]
                result.append(x)
        return result
        