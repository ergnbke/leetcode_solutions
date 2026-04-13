class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1: return False
        the_dic = {
            "(": 0,
            ")": 1,
            "{": 2,
            "}": 3,
            "[": 4,
            "]": 5
        }
        temp_str:String = ""
        for i in range(len(s)):
            if the_dic[s[i]]%2 == 0: temp_str += s[i]
            else:
                if temp_str == "": return False
                if the_dic[temp_str[len(temp_str)-1]] != the_dic[s[i]]-1: return False
                else: temp_str = temp_str[:-1]
        if temp_str != "": return False
        return True
