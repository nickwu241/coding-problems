# https://www.lintcode.com/problem/tower-of-hanoi/description
class Solution:
    """
    @param n: the number of disks
    @return: the order of moves
    """
    def towerOfHanoi(self, n):
        # write your code here
        if n == 1:
            return ['from A to C']
        def move(start, mid, end, n):
            if n == 2:
                return [
                    'from {} to {}'.format(start, mid),
                    'from {} to {}'.format(start, end),
                    'from {} to {}'.format(mid, end)
                ]
            return move(start, end, mid, n-1) + \
                ['from {} to {}'.format(start, end)] + \
                move(mid, start, end, n-1)

        return move('A', 'B', 'C', n)
