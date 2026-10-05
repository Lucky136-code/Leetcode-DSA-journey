class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        answer = 0
        for num in nums:
            answer = answer^num
        return(answer)
