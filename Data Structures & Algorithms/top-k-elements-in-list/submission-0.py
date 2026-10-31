class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count the elements first
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        # push all the values to a max heap
        heap = []
        for key in d:
            # prio, value
            heapq.heappush(heap, (-1 * d[key], key))

        result = []
        # keep poping out the value from the max heap
        for i in range(0 , k):
            result.append(heapq.heappop(heap)[1])

        return result
        