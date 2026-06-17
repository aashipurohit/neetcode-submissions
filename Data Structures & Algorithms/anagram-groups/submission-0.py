class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            sort1 = ''.join(sorted(i))
            result[sort1].append(i)
        return list(result.values())
                

        