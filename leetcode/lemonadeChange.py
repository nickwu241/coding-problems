# https://leetcode.com/problems/lemonade-change/
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        n_5_bills = 0
        n_10_bills = 0
        for payment_bill in bills:
            if payment_bill == 5:
                n_5_bills += 1
            elif payment_bill == 10:
                if n_5_bills == 0:
                    return False
                n_10_bills += 1
                n_5_bills -= 1
            elif payment_bill == 20:
                change = 15
                if n_10_bills > 0:
                    n_10_bills -= 1
                    change -= 10
                if n_5_bills < (change /5):
                    return False
                n_5_bills -= (change / 5)
            else:
                raise ValueError('unable to handle amount paid: ' + str(payment_bill))
        return True
