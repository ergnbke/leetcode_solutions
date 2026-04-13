class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j:int = 0
        for i in range(len(nums)):
            if nums[i] == val:
                j -= 1
            else:
                nums[j] = nums[i]
            j += 1
        return j
