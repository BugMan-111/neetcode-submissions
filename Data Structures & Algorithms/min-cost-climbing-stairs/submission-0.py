class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.recur(cost, 0), self.recur(cost, 1))
        


    def recur(self, cost, counter):
        # if finished climb the stairs
        if counter >= len(cost):
            return 0
        return min(self.recur(cost, counter + 1), self.recur(cost, counter + 2)) + cost[counter]