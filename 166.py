"""
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
如果小数部分为循环小数，则将循环的部分括在括号内。
如果存在多个答案，只需返回 任意一个 。
对于所有给定的输入，保证 答案字符串的长度小于 104 。

示例 1：
    输入：numerator = 1, denominator = 2
    输出："0.5"

示例 2：
    输入：numerator = 2, denominator = 1
    输出："2"

示例 3：
    输入：numerator = 2, denominator = 3
    输出："0.(6)"

示例 4：
    输入：numerator = 4, denominator = 333
    输出："0.(012)"

示例 5：
    输入：numerator = 1, denominator = 5
    输出："0.2"

提示：
    -2^31 <= numerator, denominator <= 2^31 - 1
    denominator != 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        sign = "-" if (numerator > 0 > denominator) or (numerator < 0 < denominator) else ""
        res = []
        numerator, denominator = abs(numerator), abs(denominator)
        numerator2id = {}
        idx = 0
        while numerator and numerator not in numerator2id:
            numerator2id[numerator] = idx
            if numerator < denominator:
                res.append('0')
            else:
                div, numerator = divmod(numerator, denominator)
                res.append(str(div))
            numerator = numerator * 10
            idx += 1

        if numerator in numerator2id:
            res.insert(numerator2id[numerator], "(")
            res.append(")")
        if idx > 1:
            res.insert(1, ".")
        if sign:
            res.insert(0, "-")

        return "".join(res)


numerator, denominator = -50, 8
print(Solution().fractionToDecimal(numerator, denominator))
