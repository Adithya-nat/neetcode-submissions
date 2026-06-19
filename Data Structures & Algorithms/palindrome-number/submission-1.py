class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or ( x % 10 == 0 and x != 0):
            return False
        
        rh = 0

        while x > rh:
            digit = x % 10
            rh = ( rh * 10 ) + digit
            x = x // 10
        
        return x == rh or x == (rh // 10)
        