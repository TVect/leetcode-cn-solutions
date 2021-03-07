"""
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。
如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

示例 1:
    输入:
        s = "abpcplea", d = ["ale","apple","monkey","plea"]
    输出:
        "apple"

示例 2:
    输入:
        s = "abpcplea", d = ["a","b","c"]
    输出:
        "a"

说明:
    所有输入的字符串只包含小写字母。
    字典的大小不会超过 1000。
    所有输入的字符串长度不会超过 1000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import functools
from typing import List


class Solution:

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        def mycmp(str1, str2):
            str1_size, str2_size = len(str1), len(str2)
            if str1_size > str2_size:
                return 1
            elif str1_size < str2_size:
                return -1
            else:
                return 1 if str1 < str2 else -1

        def is_subsequence(str1, str2):
            """检查 str1 是否是 str2 的子序列"""
            str1_size, str2_size = len(str1), len(str2)
            idx1, idx2 = 0, 0
            while idx1 < str1_size and idx2 < str2_size:
                if str2[idx2] == str1[idx1]:
                    idx1 += 1
                idx2 += 1
            return idx1 == str1_size

        dictionary.sort(key=functools.cmp_to_key(mycmp), reverse=True)
        for item in dictionary:
            if is_subsequence(item, s):
                return item
        return ""


s, d = "abpcplea", ["ale", "apple", "monkey", "plea", "monke"]
print(Solution().findLongestWord(s, d))
