# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def is_lte(word1, word2, char_order_map):
            """Returns true if word1 <= word2 using the char_order_map."""
            for c1, c2 in zip(word1, word2):
                if char_order_map[c1] < char_order_map[c2]:
                    return True
                elif char_order_map[c1] > char_order_map[c2]:
                    return False
            return len(word1) <= len(word2)
            
        char_order_map = {char: i for i, char in enumerate(order)}
        return all(is_lte(w1, w2, char_order_map) for w1, w2 in zip(words, words[1:]))
