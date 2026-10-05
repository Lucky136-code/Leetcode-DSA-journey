class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        answer = 0
        for nums in nums:
            answer = answer^nums
        return(answer)
