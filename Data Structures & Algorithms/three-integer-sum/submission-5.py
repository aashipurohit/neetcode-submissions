class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        l = len(nums)
        count = {}
        nums.sort()
        for i in nums:
            count[i] = count.get(i,0)+1
        for i in range(l):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,l):
                count[nums[j]] -= 1
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                third = -(nums[i]+nums[j])
                if third in count and count[third] > 0:
                    temp = [nums[i],nums[j],third]
                    result.append(temp)
            
            for j in range(i+1,l):
                count[nums[j]] += 1
        return result
        
        