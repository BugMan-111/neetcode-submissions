class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) == 1:
            return [0]
        stack = [ [len(heights) - 1, heights[len(heights) - 1]] ]
        result = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > stack[-1][1]:
                # find a higher one than stack
                stack.append([i, heights[i]])
                result.append(i)
            else:
                continue
        result.reverse()
        return result

        