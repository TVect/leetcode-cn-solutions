"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 

提示：
输入的字符串长度不会超过 1000 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 中心扩展法的扩展: Manacher Algorithm
    def countSubstrings(self, s: str) -> int:
        s = "#" + "#".join(s) + "#"
        s_size = len(s)
        arms = [0] * s_size
        center, most_right = 0, 0
        for idx in range(s_size):
            mirror = 2 * center - idx
            span = min(arms[mirror], most_right - idx)
            while True:
                if not (idx + span + 1 < s_size and idx - span - 1 >= 0 and s[idx + span + 1] == s[idx - span - 1]):
                    break
                span += 1
            arms[idx] = span
            if idx + span > most_right:
                most_right = idx + span
                center = idx
        return sum(([(arm_length + 1) // 2 for arm_length in arms]))


# s = "aaa"
s = "abc"
print(Solution().countSubstrings(s))
