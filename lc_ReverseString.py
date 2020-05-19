class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev_str = 0
        if x > 0:
            neg_ind = 1
        else:
            neg_ind = -1

        while x:
            if x > 0:
                rev_str = rev_str * 10 + x % 10
                x = int(x / 10)
            else:
                x *= -1
                rev_str = rev_str * 10 + x % 10
                rev_str *= 1
                x = int(x / 10)

        if int(rev_str) >= 2 ** 31 - 1 or int(rev_str) <= -2 ** 31:
            return 0
        else:
            return int(rev_str) * neg_ind