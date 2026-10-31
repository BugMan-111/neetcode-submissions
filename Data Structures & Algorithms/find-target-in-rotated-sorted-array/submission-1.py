class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[-1]:
                l = m + 1
            elif nums[m] < nums[-1]:
                r = m - 1
            else:
                break
        low = l

        def search(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1

        return max(search(0, low - 1), search(low, len(nums) - 1))
        