class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        result = defaultdict(list)
        for i in strs:
            count = [0]*26
            for j in i:
                z = ord(j) - ord('a')
                count[z] += 1
            key = tuple(count)
            result[key].append(i)
        return list(result.values())
                

        