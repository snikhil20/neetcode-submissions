class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        a=[0] * len(nums)
        zero_count = nums.count(0)
        if zero_count > 1:
            return a
        for num in nums:
            if num != 0:
                product=product*num
        for i in range(0, len(nums)):
           if zero_count == 1:
            a[i] = product if nums[i] == 0 else 0
           else:
            a[i]=product//nums[i]
        return a
