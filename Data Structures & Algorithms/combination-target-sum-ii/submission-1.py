class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def recur(nums, current, target, s_prev, prev, result, s):
            if  s_prev >= target:
                if s_prev == target and tuple(prev) not in s:
                    result.append(prev)
                    s.add(tuple(prev))
            for i in range(current + 1, len(nums)):
                current = deepcopy(prev)
                current.append(nums[i])
                current.sort()
                recur(nums, i, target, sum(current), current, result, s)

        result = []
        recur(candidates, -1, target, 0, [], result, set())

        print(result)

        return result
                    

            
            
            
        