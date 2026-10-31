class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right = []
        right_to_left = []

        # left to right
        value = 1
        for num in nums:
            value *= num
            left_to_right.append(value)

        # right to left
        value = 1
        for num in reversed(nums):
            value *= num
            right_to_left.append(value)
        right_to_left.reverse()

        print(left_to_right)
        print(right_to_left)

        result = []
        for i in range(0, len(nums)):
            left = left_to_right[i - 1] if i - 1 >= 0 else 1
            right = right_to_left[i + 1] if i + 1 < len(nums) else 1
            result.append(left * right)


        return result 


        

        
        