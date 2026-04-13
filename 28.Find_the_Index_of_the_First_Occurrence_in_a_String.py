class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #if len(haystack) < len(needle): return -1
        j:int = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[j]:
                j += 1
                while j < len(needle):
                    if len(haystack) < i+j+1:
                        return -1
                    if haystack[i+j] != needle[j]:
                        i += j
                        j = 0
                        break
                    j += 1
                if j != 0: return i
        return -1
