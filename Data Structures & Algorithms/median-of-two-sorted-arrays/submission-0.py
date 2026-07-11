class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median_ = nums1+nums2
        n = len(median_)
        median_.sort()
        if n%2 == 0:
            x = (median_[n//2 - 1] + median_[n//2])/2
            return x
        else:
            return median_[n//2]
        
    
        