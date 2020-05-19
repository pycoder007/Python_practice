class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x % 10 == 0 and x != 0): return False
        rev_str = 0
        while rev_str < x:
            temp = x % 10
            x = x // 10
            rev_str = rev_str * 10 + temp

        if x == rev_str or x == rev_str // 10:
            return True
        else:
            return False

