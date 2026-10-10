class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s=set(nums)
        nums[:]=sorted(s)
        return(len(nums))