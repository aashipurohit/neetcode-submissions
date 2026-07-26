class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for ch in s:
            if ch.isalnum():
                res.append(ch)
        all_join = "".join(res)
        all_lower = all_join.lower()
        j = len(all_lower)-1
        for i in range(len(all_lower)//2):
            if all_lower[i] != all_lower[j]:
                return False
            j -= 1

        return True

        

