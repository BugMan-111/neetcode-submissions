class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            currentVal = numbers[start] + numbers[end]
            if currentVal > target:
                end -= 1
            elif currentVal < target:
                start += 1
            else:
                return [start + 1, end + 1]
        
        return [-1,-1]