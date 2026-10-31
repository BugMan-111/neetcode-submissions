class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # anagram is a string contains exact same character
        # alphabet and num count should be able to match

        d_s = {}
        d_t = {}

        # map string s into dict
        for char in s:
            if char in d_s:
                d_s[char] += 1
            else:
                d_s[char] = 1

        # map string t into dict:
        for char in t:
            if char in d_t:
                d_t[char] += 1
            else:
                d_t[char] = 1


        # check the nums of keys are the same
        if len(d_s) != len(d_t):
            return False

        # if the keys are matched, check the num count
        for key_s in d_s:
            if key_s not in d_t:
                return False
            if d_s[key_s] != d_t[key_s]:
                return False

        return True
        