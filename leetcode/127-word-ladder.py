# https://leetcode.com/problems/word-ladder/
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def get_neighbours(word, next_words):
            for i in range(len(word)):
                src = word[:i] + '?' + word[i+1:]
                yield from next_words.pop(src, [])
        
        next_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                src = word[:i] + '?' + word[i+1:]
                next_words[src].append(word)

        q = deque([beginWord])
        steps = 1
        while q:
            for _ in range(len(q)):
                current_word = q.popleft()
                if current_word == endWord:
                    return steps
                for neighbour in get_neighbours(current_word, next_words):
                    q.append(neighbour)
            steps += 1
        return 0
