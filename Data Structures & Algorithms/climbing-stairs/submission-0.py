class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        current = 1

        for i in range(1 , n):
            temp = current
            current = current + prev
            prev = temp

        return current


# n = 1, current = 1
# n = 2, current = 2
        