class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        bas = 0
        while temp > 0:
            temp = temp // 10
            bas+=1
        temp = x
        for i in range(0,bas//2):
            b_dig = temp // pow(10,bas-1)
            s_dig = temp % 10
            if b_dig != s_dig:
                return False
            else:
                temp = (temp % pow(10,bas-1))
                temp = temp // 10
                bas = bas -2
        return True
