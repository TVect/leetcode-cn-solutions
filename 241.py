"""
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。
有效的运算符号包含 +, - 以及 * 。

示例 1:
    输入: "2-1-1"
    输出: [0, 2]
    解释:
        ((2-1)-1) = 0
        (2-(1-1)) = 2

示例 2:
    输入: "2*3-4*5"
    输出: [-34, -14, -10, -10, 10]
    解释:
        (2*(3-(4*5))) = -34
        ((2*3)-(4*5)) = -14
        ((2*(3-4))*5) = -10
        (2*((3-4)*5)) = -10
        (((2*3)-4)*5) = 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    # 分治法：按运算符分为左右两部分, 分别求解
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for idx in range(len(input)):
            if input[idx] in "+-*":
                left_vals = self.diffWaysToCompute(input[:idx])
                right_vals = self.diffWaysToCompute(input[idx+1:])
                for left_val in left_vals:
                    for right_val in right_vals:
                        if input[idx] == "+":
                            res.append(left_val + right_val)
                        elif input[idx] == "-":
                            res.append(left_val - right_val)
                        elif input[idx] == "*":
                            res.append(left_val * right_val)
        return res


inputs = "2-1-1"
inputs = "2*3-4*5"
print(Solution().diffWaysToCompute(inputs))
