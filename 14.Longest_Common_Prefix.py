class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i:int = 0
        the_str:String = ""
        while True:
            if len(strs[0]) < i+1:
                return the_str
            temp_str:String = strs[0][i]
            for j in strs:
                if len(j) < i+1:
                    return the_str
                if j[i] != temp_str:
                    return the_str
            the_str += temp_str
            i+=1
