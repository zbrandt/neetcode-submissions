class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = defaultdict(int)

        for n in nums:
            groups[n] += 1

        freqs = [i[0] for i in sorted(groups.items(), key=lambda item: item[1])] 
        return freqs[(len(freqs) - k):]
        