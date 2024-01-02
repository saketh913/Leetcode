#leetcode problem no:69 sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        left=1
        right=x
        
        while left<=right:
            mid=left+(right-left)//2
            if(mid*mid)==x:
                return mid
                
                
            elif(mid*mid)<x:
                left=mid+1
            else:
                right=mid-1
        return right
