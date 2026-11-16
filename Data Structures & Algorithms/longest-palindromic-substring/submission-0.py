class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        # odd pal
        for i in range(0, len(s) - 1):
            # i and j are the centre of the pal
            left, right = i, i + 1
            # we decrement the left and increment the right
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                if len(s[left : right + 1]) > len(res):
                    res = s[left : right + 1]
                left -= 1
                right += 1
        # odd pal
        for i in range(0, len(s)):
            # i and j are the centre of the pal
            left, right = i, i
            # we decrement the left and increment the right
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                if len(s[left : right + 1]) > len(res):
                    res = s[left : right + 1]
                left -= 1
                right += 1
        return res

            