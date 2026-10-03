class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left_half=nums[:mid]
        right_half=nums[mid:]
        sorted_left=self.sortArray(left_half)
        sorted_right=self.sortArray(right_half)
        return self.merge(sorted_left,sorted_right)
    def merge(self,left:List[int],right:List[int])->List[int]:
        sorted_array=[]
        i=0
        j=0
        while i<len(left) and j < len(right):
            if left[i]<right[j]:
                sorted_array.append(left[i])
                i+=1
            else:
                sorted_array.append(right[j])
                j+=1
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        return sorted_array





        