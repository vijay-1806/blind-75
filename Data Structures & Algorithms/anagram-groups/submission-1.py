class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g={}
        for i in strs:
            s=''.join(sorted(i))
            if s in g:
                g[s].append(i)
            else:
                g[s]=[i]
        return list(g.values())
