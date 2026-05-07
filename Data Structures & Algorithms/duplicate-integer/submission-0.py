class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        c=len(nums)
        cs=len(set(nums))
        if c==cs: 
            return False
        else: 
            return True
