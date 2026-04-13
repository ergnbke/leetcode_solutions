class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numss:List[int] = [0]
        numss[0]= nums[0]
        for i in nums:
            if i != numss[len(numss)-1]:
                numss.append(i)
                nums[len(numss)-1] = i
        return len(numss)
