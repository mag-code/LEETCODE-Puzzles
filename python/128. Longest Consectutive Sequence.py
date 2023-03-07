class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset, longest = set(nums),0
        for i in nums:
            if (i-1) not in numset:
                length = 1
                while (i+length) in numset:
                    length+=1
                longest=max(length,longest)
        return longest