# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
import collections

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        target = collections.Counter(p)
        subject = collections.Counter(s[:len(p)-1])
        result = []
        for i in range(len(s)-len(p)+1):
            new_letter = s[i+len(p)-1]
            if new_letter not in subject:
                subject[new_letter] = 0
            subject[new_letter] += 1

            if subject == target:
                result.append(i)

            old_letter = s[i]
            subject[old_letter] -= 1
            if subject[old_letter] == 0:
                subject.pop(old_letter)

        return result
