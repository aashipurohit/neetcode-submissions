class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        l = len(nums)
        nums.sort()
        for i in range(l):
            if i and nums[i] == nums[i-1]:
                continue
            j , k = i+1 , l-1
            while j < k :
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ > 0:
                    k -= 1
                elif sum_ < 0:
                    j += 1
                else:
                    x = [nums[i],nums[j],nums[k]]
                    result.append(x)
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return result
                    
