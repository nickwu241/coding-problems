# https://leetcode.com/problems/longest-absolute-file-path/description/
class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        running_max = 0
        depths = {0: 0}
        for line in input.split('\n'):
            basename = line.lstrip('\t')
            depth = len(line) - len(basename)
            if '.' in line:
                running_max = max(running_max, depths[depth]+len(basename))
            else:
                depths[depth+1] = depths[depth] + len(basename) + 1
        return running_max
