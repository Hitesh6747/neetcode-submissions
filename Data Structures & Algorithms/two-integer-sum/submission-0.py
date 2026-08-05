class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bakbak={}
        for i in range(len(nums)):
           rem = target-nums[i]
           if rem in bakbak:
            return [bakbak[rem],i]
           bakbak[nums[i]]=i

        