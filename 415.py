"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

提示：
    num1 和num2 的长度都小于 5100
    num1 和num2 都只包含数字 0-9
    num1 和num2 都不包含任何前导零
    你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        num1_size, num2_size = len(num1), len(num2)
        addition = 0
        res = []
        for idx in range(max(num1_size, num2_size)):
            summation = addition
            if idx < num1_size:
                summation += int(num1[-1-idx])
            if idx < num2_size:
                summation += int(num2[-1-idx])
            addition, mod = divmod(summation, 10)
            res.append(f"{mod}")
        if addition:
            res.append(f"{addition}")
        return "".join(res[::-1])


num1, num2 = "123", "456"
print(Solution().addStrings(num1, num2))
