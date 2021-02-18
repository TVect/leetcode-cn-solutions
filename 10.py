"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

示例 1：
    输入：s = "aa" p = "a"
    输出：false
    解释："a" 无法匹配 "aa" 整个字符串。

示例 2:
    输入：s = "aa" p = "a*"
    输出：true
    解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3：
    输入：s = "ab" p = ".*"
    输出：true
    解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4：
    输入：s = "aab" p = "c*a*b"
    输出：true
    解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5：
    输入：s = "mississippi" p = "mis*is*p*."
    输出：false

提示：
    0 <= s.length <= 20
    0 <= p.length <= 30
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
    保证每次出现字符 * 时，前面都匹配到有效的字符

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        s_size = len(s)
        p_size = len(p)

        memo = {}

        def helper(s_idx, p_idx):
            # print(s_idx, p_idx)
            # 返回 s[:s_idx] 和 p[:p_idx] 是否能完成匹配
            if p_idx == 0:
                return s_idx == 0
            if s_idx == 0:
                if p_idx != 0 and (p[p_idx-1] != '*'):
                    return False
            if (s_idx, p_idx) not in memo:
                if p[p_idx-1] == '.' or (s_idx > 0 and p[p_idx-1] == s[s_idx-1]):
                    memo[s_idx, p_idx] = helper(s_idx-1, p_idx-1)
                elif p[p_idx-1] == '*':
                    # _* 匹配0次 或者 _* 匹配多次
                    if s_idx > 0:
                        memo[s_idx, p_idx] = helper(s_idx, p_idx-2) or \
                                         (p[p_idx-2] in [".", s[s_idx-1]] and helper(s_idx-1, p_idx))
                    else:
                        memo[s_idx, p_idx] = helper(s_idx, p_idx - 2)
                else:
                    memo[s_idx, p_idx] = False
            # print(s_idx, p_idx, memo[s_idx, p_idx])
            return memo[s_idx, p_idx]

        return helper(s_size, p_size)


s, p = "aa", "a"
s, p = "aa", "a*"
s, p = "ab", ".*"
s, p = "aab", "c*a*b"
s, p = "mississippi", "mis*is*p*."
s, p = "a", ".*..a*"
s, p = "", ".*"
print(Solution().isMatch(s, p))
