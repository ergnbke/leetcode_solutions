class Solution:
    def romanToInt(self, s: str) -> int:
        the_dic = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        res:int = 0
        leng:int = len(s)
        for i in range(leng):
            if i == leng-1:
                res+=the_dic[s[i]]
            else:
                if the_dic[s[i]] < the_dic[s[i+1]]:
                    res -= the_dic[s[i]]
                else:
                    res += the_dic[s[i]]
        return res
