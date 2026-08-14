class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sex=set()
        for i in range(len(nums)):
            if nums[i] in sex:
                return nums[i]
            else:
                sex.add(nums[i])
        