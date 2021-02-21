"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
    输入：n = 3
    输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
    输入：n = 1
    输出：["()"]

提示：
    1 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 回溯法
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrace(partial, left_parenthesis_cnt, right_parenthesis_cnt):
            if left_parenthesis_cnt == n and right_parenthesis_cnt == n:
                res.append(partial)
            else:
                if left_parenthesis_cnt < n:
                    # 如果左括号没有用完, 则可以插入左括号
                    backtrace(partial+'(', left_parenthesis_cnt+1, right_parenthesis_cnt)
                if right_parenthesis_cnt < left_parenthesis_cnt:
                    # 如果右括号数量小于左括号数量, 则可以插入右括号
                    backtrace(partial+')', left_parenthesis_cnt, right_parenthesis_cnt+1)

        backtrace('', left_parenthesis_cnt=0, right_parenthesis_cnt=0)
        return res


n = 3
print(Solution().generateParenthesis(n))
