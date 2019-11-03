# https://leetcode.com/problems/alphabet-board-path/
from collections import deque

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # Solution without caching previous results.
        
        def get_neighbours(row, col):
            for drow, dcol, direction in ((1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')):
                new_row = row + drow 
                new_col = col + dcol
                if (0 <= new_row < 5 and 0 <= new_col < 5) or (new_row == 5 and new_col == 0):
                    yield new_row, new_col, direction
        
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        q = deque([(0, 0, [])])
        target_i = 0
        while q:
            current_row, current_col, path = q.popleft()
            current_letter = board[current_row][current_col]
            target_letter = target[target_i]
            if current_letter == target_letter:
                path.append('!')
                target_i += 1
                if target_i == len(target):
                    return ''.join(path)
                # Deal with double letters.
                q = deque([(current_row, current_col, path)])
                continue

            for next_row, next_col, next_direction in get_neighbours(current_row, current_col):
                q.append((next_row, next_col, path + [next_direction]))
        
        return None
