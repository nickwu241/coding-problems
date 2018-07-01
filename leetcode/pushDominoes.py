# https://leetcode.com/problems/push-dominoes/description/
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        last_letter = 'L'
        last_letter_i = -1
        list_dominoes = list(dominoes)
        for i, dominoe in enumerate(list_dominoes + ['R']):
            if dominoe == '.':
                continue
            
            if dominoe == 'L' and last_letter == 'R': # R...L
                lo = last_letter_i + 1
                hi = i -1
                while lo < hi:
                    list_dominoes[lo] = 'R'
                    list_dominoes[hi] = 'L'
                    lo += 1
                    hi -= 1
            elif dominoe == 'L': # L...L
                for j in range(last_letter_i + 1, i):
                    list_dominoes[j] = 'L'
            elif dominoe == 'R' and last_letter == 'R': # R...R
                for j in range(last_letter_i + 1, i):
                    list_dominoes[j] = 'R'
            last_letter = dominoe
            last_letter_i = i
        return ''.join(list_dominoes)
