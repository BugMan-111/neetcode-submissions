class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        current = 1
        l,r = 0,0
        se = set()
        se.add(s[0])
        result = 1
        while r < len(s) - 1:
            if s[r+1] in se:
                # a dup is found, move windows to the right
                se.remove(s[l])
                l += 1
                current -= 1
            else:
                se.add(s[r+1])
                current += 1
                r += 1
            print(current)
            result = max(result, current)
        return result




        