# https://www.lintcode.com/problem/next-closest-time/description
class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    def nextClosestTime(self, time):
        # write your code here
        h1, h2, m1, m2 = (int(char) for char in time if char != ':')
        digits = set([h1, h2, m1, m2])
        min_digit = min(digits)

        m2_replace = [d for d in digits if d > m2]
        if m2_replace:
            return '{}{}:{}{}'.format(h1, h2, m1, min(m2_replace))

        m1_replace = [d for d in digits if d > m1 and d <= 5]
        if m1_replace:
            return '{}{}:{}{}'.format(h1, h2, min(m1_replace), min_digit)
        
        if h1 == 2:
            h2_replace = [d for d in digits if d > h2 and d <= 3]
        else:
            h2_replace = [d for d in digits if d > h2]
            
        if h2_replace:
            return '{}{}:{}{}'.format(h1,min(h2_replace),min_digit,min_digit)

        h1_replace = [d for d in digits if d > h1 and d <= 2]
        if h1_replace:
            return '{}{}:{}{}'.format(min(h1_replace),min_digit,min_digit,min_digit)
            
        return '{}{}:{}{}'.format(min_digit,min_digit,min_digit,min_digit)
