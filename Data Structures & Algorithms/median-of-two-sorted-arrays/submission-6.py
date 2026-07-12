class Solution:
    def findMedianSortedArrays(self, num1, num2):
        prev = 0
        current = 0
        i , j = 0 , 0
        count = 0
        m , n = len(num1) , len(num2)
        half = (m+n)//2
        while count < half+1:
            if i >= m:
                x = num2[j]
                j += 1
            elif j >= n:
                x = num1[i]
                i += 1
            elif num1[i] < num2[j]:
                x = num1[i]
                i += 1
            else:
                x = num2[j]
                j += 1
            prev = current
            current = x
            count += 1
                
        if (m+n)%2 == 0:
            return (current+prev)/2
        else:
            return current
