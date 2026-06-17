class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cope = []
        for i,num in enumerate(nums):
            cope.append([num,i])
        cope.sort()

        i , j = 0, len(nums)-1
        while i < j:
            sumofnums = cope[i][0] + cope[j][0] 
            if sumofnums == target:
                return [min(cope[i][1],cope[j][1]),
                        max(cope[i][1],cope[j][1])]
            elif sumofnums < target :
                i += 1
            else:
                j -= 1
        return []
        
            
             
        

        