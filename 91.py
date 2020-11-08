"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
题目数据保证答案肯定是一个 32 位的整数。

示例 1：
    输入："12"
    输出：2
    解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2：
    输入："226"
    输出：3
    解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
示例 3：
    输入：s = "0"
    输出：0
示例 4：
    输入：s = "1"
    输出：1
示例 5：
    输入：s = "2"
    输出：1

提示：
    1 <= s.length <= 100
    s 只包含数字，并且可以包含前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def numDecodings_1(self, s: str) -> int:
        decoding_paths = [1, 1] + [0] * len(s)
        for idx in range(0, len(s)):
            if s[idx] != '0':
                decoding_paths[idx+2] += decoding_paths[idx+1]
            if idx >= 1 and s[idx - 1] != '0' and s[idx - 1: idx + 1] <= '26':
                decoding_paths[idx+2] += decoding_paths[idx]
        return decoding_paths[-1]

    # 内存优化的动态规划
    def numDecodings(self, s: str) -> int:
        prev2_cnt, prev1_cnt = 1, 1
        for idx in range(0, len(s)):
            tmp_cnt = 0
            if s[idx] != '0':
                tmp_cnt += prev1_cnt
            if idx >= 1 and s[idx-1] != '0' and s[idx-1: idx+1] <= '26':
                tmp_cnt += prev2_cnt
            prev1_cnt, prev2_cnt = tmp_cnt, prev1_cnt
        return prev1_cnt


s = "226"
# s = "2101"
print(Solution().numDecodings(s))
