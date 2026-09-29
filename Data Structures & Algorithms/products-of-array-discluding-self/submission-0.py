class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n
        right=[1]*n
        prefix=1
        for i,num in enumerate(nums):
            left[i]=prefix
            prefix*=num
        suffix=1
        for i,num in reversed(list(enumerate(nums))):
            right[i]=suffix
            suffix*=num
        result=[1]*n
        for i in range(n):
            result[i]=left[i]*right[i]
        return result