"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:
    输入: dividend = 10, divisor = 3
    输出: 3
    解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:
    输入: dividend = 7, divisor = -3
    输出: -2
    解释: 7/-3 = truncate(-2.33333..) = -2
 
提示：
    被除数和除数均为 32 位有符号整数。
    除数不为 0。
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^{31},  2^{31} − 1]。本题中，如果除法结果溢出，则返回 2^{31} − 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 递归
    def divide_1(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        multipers = [[divisor, 1]]
        while True:
            tmp = multipers[-1][0] + multipers[-1][0]
            if tmp > dividend:
                break
            multipers.append([tmp, multipers[-1][1] + multipers[-1][1]])

        residue, ret = dividend, 0
        for multiper in multipers[::-1]:
            while multiper[0] <= residue:
                ret += multiper[1]
                residue -= multiper[0]
        if sign:
            ret = - ret
        return ret if -pow(2, 31) <= ret <= pow(2, 31) - 1 else pow(2, 31)-1

    # 原码除法运算
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        count = 0
        while divisor <= dividend:
            divisor <<= 1
            count += 1

        ret, residue = 0, dividend
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= residue:
                residue -= divisor
                ret += (1 << count)
        if sign:
            ret = - ret
        return ret if -(1 << 31) <= ret <= (1 << 31)-1 else (1<<31)-1


dividend, divisor = 17, -3
print(Solution().divide(dividend, divisor))
