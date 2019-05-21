# https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.has_word(board, word, row, col):
                    return True
        return False

    def has_word(self, board, word, row, col):
        if word[0] != board[row][col]:
            return False
        next_word = word[1:]
        if not next_word:
            return True
        
        board[row][col] = None
        for next_row, next_col in self.get_neighbors(board, row, col):
            if self.has_word(board, next_word, next_row, next_col):
                return True
        board[row][col] = word[0]
        return False

    def get_neighbors(self, board, row, col):
        n_rows = len(board)
        n_cols = len(board[0])
        for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_row = row + drow
            new_col = col + dcol
            if 0 <= new_row < n_rows and 0 <= new_col < n_cols:
                yield new_row, new_col
