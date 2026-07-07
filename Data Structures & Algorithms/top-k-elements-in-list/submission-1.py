class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        heap = []
        for num in counts.keys():
            # push (count, number) onto heap, with count as the value
            heapq.heappush(heap, (counts[num], num))
            if len(heap) > k:
                # discard smallest values from heap until only k remaining
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        