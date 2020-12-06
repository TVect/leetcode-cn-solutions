"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。
字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格。整数除法仅保留整数部分。

示例 1:
    输入: "3+2*2"
    输出: 7

示例 2:
    输入: " 3/2 "
    输出: 1

示例 3:
    输入: " 3+5 / 2 "
    输出: 5

说明：
    你可以假设所给定的表达式都是有效的。
    请不要使用内置的库函数 eval。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 记录前一次的 运算符号(+-*/), 和当前次的数字:
    #   +或者-时，将当前数值或者当前数值的负值 加入到堆栈
    #   *或者/时，弹出堆栈元素做相应操作，将结果压入栈
    # 如果有括号可以采用递归调用的方式.
    # 最终的值为 栈中所有元素的求和
    def calculate(self, s: str) -> int:
        op = "+"
        stack = []
        idx, s_size = 0, len(s)
        while idx < s_size:
            if s[idx].isdigit():
                jdx = idx
                while jdx+1 < s_size and s[jdx+1].isdigit():
                    jdx += 1
                if op == "+":
                    stack.append(int(s[idx: jdx+1]))
                elif op == "-":
                    stack.append(-int(s[idx: jdx+1]))
                elif op == "*":
                    stack[-1] *= int(s[idx: jdx+1])
                elif op == "/":
                    stack[-1] = int(stack[-1] / int(s[idx:jdx+1]))
                idx = jdx
            elif s[idx] in "+-*/":
                op = s[idx]
            idx += 1

        return sum(stack)


s = "3+2*2"
s = "14 - 3/2"
print(Solution().calculate(s))
