class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sex=set()
        res=[]
        for i in range(len(nums)):
            l=i+1
            right=len(nums)-1
            while l<right:
                total = (nums[i]+nums[l]+nums[right])
                if total==0:
                    sex.add((nums[i],nums[l],nums[right]))
                    l+=1
                    right-=1
                elif total >0:
                    right-=1
                else:
                    l+=1
        return [list(i) for i in sex]
                        