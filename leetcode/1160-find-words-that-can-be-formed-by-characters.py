# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def can_form_word(word, char_counter=Counter(chars)):
            used_char_counter = Counter()
            for char in word:
                used_char_counter[char] += 1
                if char not in char_counter or used_char_counter[char] > char_counter[char]:
                    return False
            return True
        
        sum_length_of_formmable_words = 0
        for word in words:
            if can_form_word(word):
                sum_length_of_formmable_words += len(word)
        return sum_length_of_formmable_words
