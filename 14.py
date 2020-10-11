"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for tmp_str in strs[1:]:
            idx = 0
            max_span = min(len(prefix), len(tmp_str))
            while idx < max_span and prefix[idx] == tmp_str[idx]:
                idx += 1
            prefix = prefix[:idx]
        return prefix


strs = ["dog", "racecar", "car"]
strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
