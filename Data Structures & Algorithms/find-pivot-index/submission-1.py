class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = []
        x = 0
        for i in range(len(nums)):
            x += nums[i]
            pre.append(x)  
        if 0 == pre[-1] - pre[0]:
                return 0
        for j in range(1,len(pre)):
            if pre[j-1] == pre[len(nums)-1] - pre[j]:
                return j
        return -1

        