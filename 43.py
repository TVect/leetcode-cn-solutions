"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"

说明：
num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 普通的竖式运算
    def multiply_1(self, num1: str, num2: str) -> str:
        patial_rets = []
        for num2_item in num2[::-1]:
            ret = [0] * len(patial_rets)
            accumulate = 0
            for num1_item in num1[::-1]:
                accumulate, mod = divmod(int(num1_item) * int(num2_item) + accumulate, 10)
                ret.append(mod)
            if accumulate != 0:
                ret.append(accumulate)
            patial_rets.append(ret)

        return_val = []
        accumulate = 0
        max_patial_length = max(len(item) for item in patial_rets)
        for idx in range(max_patial_length):
            accumulate, mod = divmod(
                sum([patial_ret[idx] if idx < len(patial_ret) else 0 for patial_ret in patial_rets]) + accumulate,
                10)
            return_val.append(mod)
        if accumulate != 0:
            return_val.append(accumulate)
        if sum(return_val) == 0:
            return '0'
        return "".join(map(str, return_val[::-1]))

    # 优化的竖式运算
    # 1. 乘数 num1 位数为 M，被乘数 num2 位数为 N， 则num1 x num2 结果 res 最大总位数为 M + N
    # 2. num1[i] x num2[j] 的结果为 tmp(位数为两位，"0x", "xy" 的形式)，其第一位位于 res[i + j]，第二位位于 res[i + j + 1]。
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1_size = len(num1)
        num2_size = len(num2)
        return_val = [0] * (num1_size + num2_size)
        for idx_1 in range(num1_size):
            for idx_2 in range(num2_size):
                return_val[idx_1+idx_2] += int(num1[num1_size-idx_1-1]) * int(num2[num2_size-idx_2-1])

        for idx in range(num1_size + num2_size - 1):
            div, mod = divmod(return_val[idx], 10)
            return_val[idx] = mod
            return_val[idx + 1] += div

        return "".join(map(str, return_val[-2::-1])) if return_val[-1] == 0 else "".join(map(str, return_val[::-1]))

    # 多项式乘法项(卷积)


num1 = '123'
num2 = '456'
print(Solution().multiply(num1, num2))
