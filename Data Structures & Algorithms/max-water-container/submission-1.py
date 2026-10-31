class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0

        # right = 4 left = 0
        while left < right:
            current = min(heights[left], heights[right]) * (right - left) 

            if current > result:
                result = current

            # always move the small ones
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return result
        