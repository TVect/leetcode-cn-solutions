"""
初始时有 n 个灯泡关闭。

第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。

第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。

找出 n 轮后有多少个亮着的灯泡。

示例 1：
    输入：n = 3
    输出：1
    解释：
        初始时, 灯泡状态 [关闭, 关闭, 关闭].
        第一轮后, 灯泡状态 [开启, 开启, 开启].
        第二轮后, 灯泡状态 [开启, 关闭, 开启].
        第三轮后, 灯泡状态 [开启, 关闭, 关闭].
        你应该返回 1，因为只有一个灯泡还亮着。

示例 2：
    输入：n = 0
    输出：0

示例 3：
    输入：n = 1
    输出：1

提示：
    0 <= n <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bulb-switcher
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import math


class Solution:

    def bulbSwitch_1(self, n: int) -> int:
        if n == 0:
            return 0
        bulb = [False] * n
        for idx in range(1, n+1):
            for jdx in range(idx-1, n, idx):
                bulb[jdx] = not bulb[jdx]
        return sum(bulb)

    def bulbSwitch(self, n: int) -> int:
        # 所以被操作 奇数次 的灯 最后是亮着的
        # 第 k 轮会操作的灯为: k, 2k, 3k, ...
        # 推而广之, 第 k 个灯有多少个因子就会被操作多少次
        # 一般情况下，因子都是成对出现，只有在完全平方数的时候才会出现奇数个因子
        # 假设现在总共有 16 盏灯，我们求 16 的平方根，等于 4，这就说明最后会有 4 盏灯亮着，
        # 它们分别是第 1*1=1 盏、第 2*2=4 盏、第 3*3=9 盏和第 4*4=16 盏。
        return int(math.sqrt(n))


n = 3
print(Solution().bulbSwitch(n))
