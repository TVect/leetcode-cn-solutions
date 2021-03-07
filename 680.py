"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:
    输入: "aba"
    输出: True

示例 2:
    输入: "abca"
    输出: True
    解释: 你可以删除c字符。

注意:
    字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def validPalindrome(self, s: str) -> bool:
        s_size = len(s)
        if s_size < 2:
            return True

        def check(left_idx, right_idx):
            while left_idx < right_idx:
                if s[left_idx] != s[right_idx]:
                    return False
                left_idx += 1
                right_idx -= 1
            return True

        left, right = 0, s_size - 1
        while left < right - 1:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return check(left, right-1) or check(left+1, right)
        return True


s = "abca"
s = "eeccccbebaeeabebccceea"
print(Solution().validPalindrome(s))
