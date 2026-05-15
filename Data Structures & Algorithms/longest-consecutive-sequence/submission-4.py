class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = set()
        res = 0
        for i in range(len(nums)):
            if nums[i] not in track:
                cur = 1
                tmp = nums[i]
                while (tmp - 1) in track:
                    tmp -= 1
                    cur += 1
                tmp = nums[i]
                while (tmp + 1) in track:
                    tmp += 1
                    cur += 1
                res = max(cur, res)
                track.add(nums[i])
        return res
        
        