class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        res=[]
        s=dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        ans=list(s)
        res=ans[:k]
        g=[]
        for i in range(k):
            g.append(res[i])
        return g
            

                    
