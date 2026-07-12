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
                prev = current
                current = num2[j]
                j += 1
                count += 1
            elif j >= n:
                prev = current
                current = num1[i]
                count += 1
                i += 1

            elif num1[i] < num2[j]:
                prev = current
                current = num1[i]
                count += 1
                i += 1
                
            else:
                prev = current
                current = num2[j]
                j += 1
                count += 1
                
        if (m+n)%2 == 0:
            return (current+prev)/2
        else:
            return current
