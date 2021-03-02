"""
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。

示例 1：
    输入：s = "1 + 1"
    输出：2

示例 2：
    输入：s = " 2-1 + 2 "
    输出：3

示例 3：
    输入：s = "(1+(4+5+2)-3)+(6+8)"
    输出：23

提示：
    1 <= s.length <= 3 * 10^5
    s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
    s 表示一个有效的表达式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 借鉴 leetcode 227 的做法，加上了对 括号 的递归调用处理
    # 会超时
    def calculate(self, s: str) -> int:

        s_list = list(s)

        def helper():
            op = "+"
            num, stack = 0, []
            while s_list:
                character = s_list.pop(0)
                if character.isdigit():
                    num = num * 10 + int(character)
                elif character == "(":
                    num = helper()

                if character in "+-*/)" or len(s_list) == 0:
                    if op == "+":
                        stack.append(num)
                    elif op == "-":
                        stack.append(-num)
                    elif op == "*":
                        stack.append(stack.pop(-1) * num)
                    elif op == "/":
                        stack.append(int(stack.pop(-1) / num))
                    num, op = 0, character

                if character == ")":
                    break
            return sum(stack)

        return helper()


s = "1 + 1"
s = " 2-1 + 2 "
s = "(1+(4+5+2)-3)+(6+8)"
# s = "(4+5+2)"
print(Solution().calculate(s))
