
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for chars in zip(*strs):
            if all(ch == chars[0] for ch in chars):
                ans += chars[0]
            else:
                return ans

        return ans
