class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        sex=set(nums)
        sex1=list(sex)
        sex1.sort()
        count=1
        max=1
        for i in range(len(sex1)-1):
            
            if sex1[i]+1==sex1[i+1]:
                count+=1
                if count>max:
                    max=count
            else:
                count=1
        return max
        