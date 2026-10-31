class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            current_value = mid ** 2
            if current_value > x:
                high = mid - 1
            elif current_value < x:
                low = mid + 1
            elif current_value == x:
                return mid
        return low - 1
        