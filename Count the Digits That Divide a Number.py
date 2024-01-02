#Leetcode problem no:2520 Count the Digits That Divide a Number


class Solution:
    def countDigits(self, num: int) -> int:
        l=num
        count=0
        while num>0:
            rem=num%10
            num=num//10
            if rem>0 and l%rem==0:
                count=count+1
        return count
