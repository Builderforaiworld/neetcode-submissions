class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for left in range(len(nums)-2):
            if left>0 and nums[left]==nums[left-1]:
                continue
            mid=left+1
            right=len(nums)-1
            while (mid<right):
                target_sum=nums[left]+nums[mid]+nums[right]
                if target_sum==0:
                    res.append([nums[left],nums[mid],nums[right]])
                    mid+=1
                    right-=1
                    while mid<right and nums[mid]==nums[mid-1]:
                        mid+=1
                elif target_sum>0:
                    right-=1
                else:
                    mid+=1
                        
        return res                        

