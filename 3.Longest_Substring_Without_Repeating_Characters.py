class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = ""
        m_len = 0
        for i in range(0,len(s)):
            if len(sub_s) == 0:
                sub_s += s[i]
                continue
            else:
                for j in range(len(sub_s)-1,-1,-1):
                    if sub_s[j] == s[i]:
                        if len(sub_s) > m_len:
                            m_len = len(sub_s)
                        temp_s =""
                        for k in range(j+1,len(sub_s)):
                            temp_s += sub_s[k]
                        sub_s = temp_s
                        sub_s += s[i]
                        break
                    if j == 0:
                        sub_s += s[i]
        return max(m_len,len(sub_s))
