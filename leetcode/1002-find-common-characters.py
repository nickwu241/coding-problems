# https://leetcode.com/problems/find-common-characters/
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        
        LENGTH_OF_ALPHABET = 26
        common_char_occurences = [float('inf')] * LENGTH_OF_ALPHABET
        for word in A:
            char_occurences = [0] * LENGTH_OF_ALPHABET
            for char in word:
                char_occurences[ord(char) - ord('a')] += 1
            for i in range(LENGTH_OF_ALPHABET):
                common_char_occurences[i] = min(
                    common_char_occurences[i],
                    char_occurences[i]
                )

        result = []
        for i in range(LENGTH_OF_ALPHABET):
            for _ in range(common_char_occurences[i]):
                result.append(chr(ord('a') + i))
        return result
