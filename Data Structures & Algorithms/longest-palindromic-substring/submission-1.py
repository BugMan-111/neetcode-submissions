class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def longest_pal(left, right):
            local_max = ""
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                if len(s[left : right + 1]) > len(local_max):
                    local_max = s[left : right + 1]
                left -= 1
                right += 1
            return local_max

        # odd pal
        for i in range(0, len(s) - 1):
            curr = longest_pal(i, i + 1)
            res = res if len(res) > len(curr) else curr
           
        # odd pal
        for i in range(0, len(s)):
            curr = longest_pal(i, i)
            res = res if len(res) > len(curr) else curr
           
        return res

            