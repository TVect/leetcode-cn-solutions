"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 

提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        num_rows = len(board)
        num_cols = len(board[0])
        len_word = len(word)

        def dfs(row, col, word_idx):
            if word_idx >= len_word:
                return True
            if 0 <= row < num_rows and 0 <= col < num_cols:
                if board[row][col] == word[word_idx]:
                    tmp = board[row][col]
                    board[row][col] = 0
                    ret = dfs(row - 1, col, word_idx + 1) or dfs(row + 1, col, word_idx + 1) or \
                          dfs(row, col - 1, word_idx + 1) or dfs(row, col + 1, word_idx + 1)
                    board[row][col] = tmp
                    return ret
                else:
                    return False
            else:
                return False

        for i in range(num_rows):
            for j in range(num_cols):
                if dfs(i, j, 0):
                    return True
        return False


board = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']]
word = "ABCCED"
print(Solution().exist(board, word))
