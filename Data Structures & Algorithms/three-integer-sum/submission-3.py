class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        l = len(nums)
        for i in range(l):
            my_set = set()
            for j in range(i+1,l):
                third = -(nums[i]+nums[j])
                if third in my_set:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add((nums[j]))
            
        return [list(ans) for ans in result]