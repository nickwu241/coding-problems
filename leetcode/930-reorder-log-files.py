# https://leetcode.com/problems/reorder-log-files/
import operator

class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit_logs = []
        letter_logs = []
        for log in logs:
            identifier, logline = log.split(' ', 1)
            if logline[0].isdigit():
                digit_logs.append(identifier + ' ' + logline)
            else:
                letter_logs.append((identifier, logline))
        letter_logs.sort(key=operator.itemgetter(1))
        return [' '.join(e) for e in letter_logs] + digit_logs
