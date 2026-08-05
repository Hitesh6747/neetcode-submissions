class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        siu=set()
        for i in range(len(nums)):
            if nums[i] in siu:
                return True
            siu.add(nums[i])
        return False
