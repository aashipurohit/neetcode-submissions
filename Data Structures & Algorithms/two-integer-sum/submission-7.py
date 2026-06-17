class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i,num in enumerate(nums):
                dif = target - num
                if dif in comp:
                    return [comp[dif],i]
                comp[num] = i
        return [-1]
        
            
             
        

        