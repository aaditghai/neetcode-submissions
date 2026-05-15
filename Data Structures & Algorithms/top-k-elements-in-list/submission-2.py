class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        sortedFreq = dict(sorted(freq.items(), key = lambda x: x[1], reverse = True))
        res = []
        for num in sortedFreq.keys():
            res.append(num)
            if len(res) >= k:
                return res
        return res




        