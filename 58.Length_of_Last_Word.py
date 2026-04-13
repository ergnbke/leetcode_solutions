class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ll:int = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ": ll += 1
            elif ll != 0: return ll
        return ll
