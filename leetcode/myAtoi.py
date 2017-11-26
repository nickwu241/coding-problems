# https://leetcode.com/problems/string-to-integer-atoi/description/
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        # skip preceding spaces
        try:
            while str[i] == ' ':
                i += 1
        except IndexError:
            return 0

        INT_MAX, INT_MAX_DIV10, INT_MIN = 2147483647, 214748364, -2147483648
        sign, base, = 1, 0

        # handle signs
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            sign = -1
            i += 1

        # AV stands for ascii value
        AV_0, AV_9 = ord('0'), ord('9')
        for i in range(i, len(str)):
            # check for non-digit
            av = ord(str[i])
            if av < AV_0 or av > AV_9:
                return base * sign

            # check for overflow
            val = av - AV_0
            if base > INT_MAX_DIV10 or (base == INT_MAX_DIV10 and val > 7):
                return INT_MAX if sign == 1 else INT_MIN

            base = base * 10 + val

        return base * sign
