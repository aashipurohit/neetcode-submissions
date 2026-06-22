class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1

        arr = []
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort()

        result = []
        for i in range(k):
            result.append(arr.pop()[1])

        return result
            


        
        