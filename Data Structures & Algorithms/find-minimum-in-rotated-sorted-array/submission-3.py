class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the rest of the array is gauranted to have a peak
        # 1 [2 3 4]
        # [4] 1 [2 3]
        # [3 4] 1 [2]
        # [2 3 4] 1

        # [top] low [bottom] 


        # 3,4,5,6,7,1,2
        # 7,1,2,3,4,5,6

        # 3 4 5 6 1 2
        # l = 0, r = 5, m = 2 m[2] = 5
        # 5 > 2
        # 

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[-1]:
                # must be on the left
                l = m + 1
            elif nums[m] < nums[-1]:
                r = m - 1
            else:
                break
        return nums[l]

       