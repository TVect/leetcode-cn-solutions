"""
给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
请你返回让 s 成为回文串的 最少操作次数 。
「回文串」是正读和反读都相同的字符串。

示例 1：
    输入：s = "zzazz"
    输出：0
    解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。

示例 2：
    输入：s = "mbadm"
    输出：2
    解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。

示例 3：
    输入：s = "leetcode"
    输出：5
    解释：插入 5 个字符后字符串变为 "leetcodocteel" 。

示例 4：
    输入：s = "g"
    输出：0

示例 5：
    输入：s = "no"
    输出：1

提示：
    1 <= s.length <= 500
    s 中所有字符都是小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 区间动态规划
    def minInsertions(self, s: str) -> int:
        # dp[i][j] 表示让 s[i, ..., j] 成为回文串的 最少操作次数 
        s_size = len(s)
        dp = [[0] * s_size for _ in range(s_size)]
        for i in range(s_size-1, -1, -1):
            for j in range(i+1, s_size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
        return dp[0][s_size-1]


s = "mbadm"
print(Solution().minInsertions(s))
