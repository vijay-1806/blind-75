class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<1:
            return False
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        l=max(d.values())
        if l>1:
            return True
        return False