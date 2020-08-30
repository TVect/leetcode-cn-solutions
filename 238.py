"""
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
 

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/product-of-array-except-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 左右乘积列表法
    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        left_product = [1] * nums_size
        right_product = [1] * nums_size
        for i in range(1, nums_size):
            left_product[i] = nums[i - 1] * left_product[i - 1]
        for i in range(nums_size - 2, -1, -1):
            right_product[i] = nums[i + 1] * right_product[i + 1]
        return [left_product[i] * right_product[i] for i in range(nums_size)]

    # 改进的左右乘积列表法：常数空间复杂度
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        rets = [1] * nums_size
        for i in range(1, nums_size):
            rets[i] = nums[i - 1] * rets[i - 1]
        right_to_now = 1
        for i in range(nums_size-2, -1, -1):
            right_to_now *= nums[i+1]
            rets[i] *= right_to_now
        return rets


nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
