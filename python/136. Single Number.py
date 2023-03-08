class Solution:
#solution 1
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for i in nums:
            single ^= i
        return nums
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            single = nums.pop(0)
            if single not in nums:
                return single 
            nums.append(single)
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                return nums[i]
            i+=2
        return nums[-1]