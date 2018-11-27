# https://leetcode.com/problems/find-and-replace-pattern/
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def does_match(word, pattern):
            mapping = {}
            mapped = set()
            for word_char, pattern_char in zip(word, pattern):
                if word_char not in mapping:
                    if pattern_char in mapped:
                        return False
                    mapping[word_char] = pattern_char
                    mapped.add(pattern_char)
                elif mapping[word_char] != pattern_char:
                    return False
            return True
        
        return [word for word in words if does_match(word, pattern)]
