class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        up = 1
        for i in range(len(digits) - 1, -1,-1):
            digits[i] += up
            if digits[i] >= 10:
                digits[i] -= 10
                up = 1
            else:
                up = 0
        if up == 1:
            digits.insert(0,1)

        return digits

        