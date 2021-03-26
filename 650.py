"""
最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：

Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
Paste (粘贴) : 你可以粘贴你上一次复制的字符。
给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。

示例 1:
    输入: 3
    输出: 3
    解释:
        最初, 我们只有一个字符 'A'。
        第 1 步, 我们使用 Copy All 操作。
        第 2 步, 我们使用 Paste 操作来获得 'AA'。
        第 3 步, 我们使用 Paste 操作来获得 'AAA'。
    说明:
        n 的取值范围是 [1, 1000] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/2-keys-keyboard
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def minSteps_1(self, n: int) -> int:
        # dp[i]: 产生长度为 i 的串所需要的最小操作次数
        dp = [float('inf')] * (n + 1)
        dp[1] = 0
        for i in range(1, n+1):
            for j in range(1, i//2 + 1):
                if i % j == 0:
                    # 最后一次 CopyALl 操作可以发生在 j 位置
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[-1]

    # 素数分解法
    def minSteps(self, n: int) -> int:
        # 操作序列为 "CPPP CPPPP CPPPP" 最终的长度为 g1 * g2 * g3 ...
        # 总的操作次数为 g1 + g2 + g3
        # 其中 g1 g2 g3 分别为 第1组 第2组 第3组 的长度
        # 根据以上分析，可以知道最短操作序列 对应着 素数分解
        res, num = 0, 2
        while n > 1:
            while n % num == 0:
                res += num
                n //= num
            num += 1
        return res


n = 18
print(Solution().minSteps(n))
