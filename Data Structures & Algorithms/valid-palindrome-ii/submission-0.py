class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while(left<right):
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                str_a=s[left+1:right+1]
                str_b=s[left:right]
                return str_a==str_a[::-1] or str_b==str_b[::-1]
        return True
            

             
        
        
                
                    
        

        

        
        