class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # two pointers
        nums.sort()
        start, end = 0, len(nums) - 1
        res = 0
        while start <= end:
            # less or equals to
            current_sum = nums[start] + nums[end]
            if current_sum > target:
                # decrease from the end
                end -= 1
            else:
                # increment the res
                # increase from the beg
                total = end - start + 1
                seq_with_start = total - 1
                res += 2 ** seq_with_start
                start += 1

        return res % (10 ** 9 + 7)
        