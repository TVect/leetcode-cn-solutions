"""
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 单调栈: 从左往右入栈
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        T_size = len(T)
        stack, rets = [], [0] * T_size
        for idx in range(T_size):
            while stack and T[idx] > T[stack[-1]]:
                prev_idx = stack.pop()
                rets[prev_idx] = idx - prev_idx
            stack.append(idx)
        return rets

    # 单调栈: 从右往左进栈
    def dailyTemperatures_1(self, T: List[int]) -> List[int]:
        T_size = len(T)
        stack, rets = [], [0] * T_size
        for idx in range(T_size-1, -1, -1):
            while stack and T[idx] >= T[stack[-1]]:
                stack.pop()
            rets[idx] = stack[-1] - idx if stack else 0
            stack.append(idx)
        return rets


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
