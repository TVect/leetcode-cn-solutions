"""
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
你的目标是确切地知道 F 的值是多少。
无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

示例 1：
    输入：K = 1, N = 2
    输出：2
    解释：
        鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
        否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
        如果它没碎，那么我们肯定知道 F = 2 。
        因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。

示例 2：
    输入：K = 2, N = 6
    输出：3

示例 3：
    输入：K = 3, N = 14
    输出：4

提示：
    1 <= K <= 100
    1 <= N <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-egg-drop
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}

        # memo[k, n]: 表示 使用 k 个鸡蛋 确定 n 个楼层，最坏情况下所需要的最小移动次数
        def helper(k, n):
            if n == 0:
                return 0
            if k == 1:
                return n
            if (k, n) not in memo:
                left, right = 1, n
                res = float('inf')

                # helper(k, n) = min([1 + max(helper(k, n - i), helper(k - 1, i - 1) for i in range(1, n + 1)])
                # helper(k, n-i): 选择从第 i 层扔鸡蛋，如果鸡蛋碎了
                # helper(k-1, i-1): 选择从第 i 层扔鸡蛋，如果鸡蛋未碎
                # 二分查找 得到 helper(k, n-i) 和 helper(k-1, i-1) 相等的值, 即为想要的 最小移动次数
                while left <= right:
                    mid = (left + right) // 2
                    val1 = helper(k, n - mid)
                    val2 = helper(k - 1, mid - 1)
                    if val1 > val2:
                        left = mid + 1
                        res = min(res, 1 + val1)
                    elif val1 < val2:
                        right = mid - 1
                        res = min(res, 1 + val2)
                    else:
                        res = min(res, 1 + val2)
                        break
                memo[(k, n)] = res
            return memo[(k, n)]

        return helper(K, N)


K, N = 1, 2
K, N = 2, 6
K, N = 3, 14
K, N = 4, 5000
K, N = 100, 8192
print(Solution().superEggDrop(K, N))
