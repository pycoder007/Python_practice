class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total_len = len(s)
        i = 0
        r = 0
        while i < len(s):
            s1 = d[s[i]]
            if i+1 < len(s):
                s2 = d[s[i+1]]

                if s1 >= s2:
                    r += s1
                    i += 1
                else:
                    r = (r + s2) - s1
                    i += 2
            else:
                r += d[s[i]]
                i += 1

        return r