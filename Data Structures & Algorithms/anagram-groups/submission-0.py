class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
      
        for i, stri in enumerate(strs):
            sorstr=''.join(sorted(stri))
            res[sorstr].append(stri)
        return list(res.values())