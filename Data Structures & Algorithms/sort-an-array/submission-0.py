class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = nums[:mid:]
        l = self.sortArray(left)
        right = nums[mid::]
        r = self.sortArray(right)
        return self.merge(l,r)

    def merge(self, l: List[int] , r: List[int])-> List[int]:
        res = []
        i , j = 0 , 0
        while i < len(l) and j < len(r):
            if l[i] > r[j]:
                res.append(r[j])
                j += 1
            else:
                res.append(l[i])
                i += 1

        x = l[i::]
        y = r[j::]
        res.extend(x)
        res.extend(y)
        return res
        
        