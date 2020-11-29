"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

进阶：
    你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?

示例 1：
    输入：nums = [3,0,1]
    输出：2
    解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 2：
    输入：nums = [0,1]
    输出：2
    解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 3：
    输入：nums = [9,6,4,2,3,5,7,0,1]
    输出：8
    解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。

示例 4：
    输入：nums = [0]
    输出：1
    解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。


提示：
    n == nums.length
    1 <= n <= 10^4
    0 <= nums[i] <= n
    nums 中的所有数字都 独一无二

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 标记法
    # 把出现过的数字，对应的位置上的数字设置为 负数. 最后只需要查找出非负数即可.
    def missingNumber_1(self, nums: List[int]) -> int:
        nums_size = len(nums)
        nums.append(nums_size)
        for idx in range(nums_size):
            if nums[idx] < 0:
                nums[-nums[idx] - 1] = -nums[-nums[idx] - 1] - 1
            else:
                nums[nums[idx]] = -nums[nums[idx]] - 1
        for idx in range(nums_size + 1):
            if nums[idx] >= 0:
                return idx

    # 求和
    def missingNumber_2(self, nums: List[int]) -> int:
        nums_size = len(nums)
        return nums_size * (nums_size + 1) // 2 - sum(nums)

    # 位运算
    def missingNumber(self, nums: List[int]) -> int:
        ret = len(nums)
        for idx, num in enumerate(nums):
            ret ^= num ^ idx
        return ret


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
nums = [2, 0]
print(Solution().missingNumber(nums))
