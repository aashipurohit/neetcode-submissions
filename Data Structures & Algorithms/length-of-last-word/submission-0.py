class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for word in range(len(s)-1,-1,-1):
            if s[word].isalpha():
                count += 1
            else:
                if count <= 0:
                    continue
                else:
                    break
        
        return count
                


        