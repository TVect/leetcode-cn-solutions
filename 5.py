"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # Manacher Algorithm : implement 1
    # 枚举了各种细节情况
    def longestPalindrome_1(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"
        s_size = len(s)
        arm_lens = [0] * s_size
        center, right_bound = 0, 0

        def calc_arm_length(cur_idx, min_len):
            while True:
                left_idx = cur_idx - min_len - 1
                right_idx = cur_idx + min_len + 1
                if not (left_idx >= 0 and right_idx < s_size and s[right_idx] == s[left_idx]):
                    break
                min_len += 1
            return min_len

        max_arm, max_arm_idx = -1, -1
        for idx in range(s_size):
            mirror = 2 * center - idx
            if idx + arm_lens[mirror] >= right_bound:
                # arm_lens[idx] 至少为 right_bound - idx, 继续扩展对比
                arm_lens[idx] = calc_arm_length(idx, right_bound - idx)
            elif mirror - arm_lens[mirror] == 0:
                # arm_lens[idx] 至少为 arm_lens[mirror], 继续扩展对比
                arm_lens[idx] = calc_arm_length(idx, arm_lens[mirror])
            elif idx == right_bound:
                # arm_lens[idx] 至少为 0, 继续扩展对比
                arm_lens[idx] = calc_arm_length(idx, 0)
            else:
                arm_lens[idx] = arm_lens[mirror]

            if idx + arm_lens[idx] > right_bound:
                right_bound = idx + arm_lens[idx]
                center = idx

            if arm_lens[idx] >= max_arm:
                max_arm = arm_lens[idx]
                max_arm_idx = idx

        # print(max_arm, max_arm_idx)
        return s[max_arm_idx - max_arm + 1 : max_arm_idx + max_arm + 1 : 2]

    # Manacher Algorithm : implement 2
    def longestPalindrome_2(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"
        s_size = len(s)
        arm_lens = [0] * s_size
        center, right_bound = 0, 0
        max_arm, max_arm_idx = -1, -1

        for idx in range(s_size):
            arm_lens[idx] = min(right_bound - idx, arm_lens[2 * center - idx])
            while True:
                left_idx = idx - arm_lens[idx] - 1
                right_idx = idx + arm_lens[idx] + 1
                if not (left_idx >= 0 and right_idx < s_size and s[right_idx] == s[left_idx]):
                    break
                arm_lens[idx] += 1

            if idx + arm_lens[idx] > right_bound:
                right_bound = idx + arm_lens[idx]
                center = idx

            if arm_lens[idx] >= max_arm:
                max_arm = arm_lens[idx]
                max_arm_idx = idx

        return s[max_arm_idx - max_arm + 1 : max_arm_idx + max_arm + 1 : 2]

    # 动态规划算法
    def longestPalindrome_3(self, s: str) -> str:
        s_size = len(s)
        if s_size == 0:
            return ""

        optimal_pos, optimal_length = 0, 1
        # dp[i][j] 表示 s[i, ..., j] 是否为回文串
        dp = [[False] * s_size for _ in range(s_size)]

        # 初始化
        for i in range(s_size):
            dp[i][i] = True

        # 动态规划
        for i in range(s_size-1, -1, -1):
            for j in range(i+1, s_size):
                if s[i] == s[j] and (j == i + 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    tmp_length = j - i + 1
                    if tmp_length > optimal_length:
                        optimal_length = tmp_length
                        optimal_pos = i
        return s[optimal_pos: optimal_pos + optimal_length]

    # 中心扩展算法
    def longestPalindrome(self, s: str) -> str:
        s_size = len(s)

        def helper(left_idx, right_idx):
            while left_idx >= 0 and right_idx < s_size and s[left_idx] == s[right_idx]:
                left_idx -= 1
                right_idx += 1
            return left_idx + 1, right_idx - left_idx - 1

        optimal_pos, optimal_length = -1, -1
        for idx in range(s_size):
            # 从 idx 向左右扩展，得到以 idx 为中心的最长回文字串
            pos1, length1 = helper(idx, idx)
            if length1 > optimal_length:
                optimal_pos, optimal_length = pos1, length1
            if idx + 1 < s_size:
                pos2, length2 = helper(idx, idx+1)
                if length2 > optimal_length:
                    optimal_pos, optimal_length = pos2, length2
        return s[optimal_pos: optimal_pos + optimal_length]


s = "babad"
# s = "cbbd"
print(Solution().longestPalindrome(s))
