class Solution:
    def containsDuplicate(self, num: list[int]) -> bool:
        seen = set()

        for x in num:
            if x in seen:
                return (True)
            seen.add(x)
        return(False)
       
