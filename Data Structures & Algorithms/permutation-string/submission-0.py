class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # make s1 a mask to check against s2
        d_s1 = {}
        for char in s1:
            if char in d_s1:
                d_s1[char] += 1
            else:
                d_s1[char] = 1

        # check against s2 with window size of s1
        if len(s1) > len(s2):
            return False

        # set the l ptr to 0 and r ptr to size of the s1
        l, r = 0, len(s1) - 1

        # count number in the window
        d_s2 = {}
        for char in s2[l : r + 1]:
            if char in d_s2:
                d_s2[char] += 1
            else:
                d_s2[char] = 1

        while r <= len(s2) - 1:
            print(d_s2)
            # check if two words counts are the same
            if d_s1 == d_s2:
                return True

            # remove the prev l and add the new r
            if r < len(s2) - 1:
                prev_l = s2[l]
                prev_right = s2[r + 1]
                # for left, if removing prev l causes d[prev] == 0
                # drop the prev char
                if d_s2[prev_l] - 1 <= 0:
                    del d_s2[prev_l]
                else:
                    d_s2[prev_l] -= 1
                # for r, always add the new char
                if prev_right not in d_s2:
                    d_s2[prev_right] = 1
                else:
                    d_s2[prev_right] += 1
            l += 1 
            r += 1

        return False
        

        