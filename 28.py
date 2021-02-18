"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
    输入: haystack = "hello", needle = "ll"
    输出: 2
示例 2:
    输入: haystack = "aaaaa", needle = "bba"
    输出: -1
说明:
    当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
    对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # KMP 算法
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        size_needle = len(needle)
        # 计算 dp: dp[i] 表示 dp[0, ..., i] 的最长公共前后缀的长度
        dp = [0] * size_needle
        for i in range(1, size_needle):
            # 考虑 needle[:i+1] 的最长公共前后缀的长度
            # 由 dp[i-1] 的定义可知：needle[:dp[i-1]] == needle[i-dp[i-1] : i]
            jdx = dp[i-1]
            while jdx > 0 and needle[i] != needle[jdx]:
                jdx = dp[jdx-1]
                # print(jdx, dp)
            dp[i] = jdx + 1 if needle[i] == needle[jdx] else 0

        # print(dp)
        size_haystack = len(haystack)
        idx, jdx = 0, 0
        while idx < size_haystack and jdx < size_needle:
            if haystack[idx] == needle[jdx]:
                idx += 1
                jdx += 1
            else:
                if jdx == 0:
                    idx += 1
                else:
                    jdx = dp[jdx-1]
            # print(idx, jdx)
        return idx-jdx if jdx == size_needle else -1


haystack, needle = "hello", "ll"
# haystack, needle = "aaaaa", "bba"
# haystack, needle = "mississippi", "issip"
# haystack, needle = "adcadcaddcadde", "adcadde"
print(Solution().strStr(haystack, needle))
