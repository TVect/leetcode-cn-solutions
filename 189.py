"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
    输入: [1,2,3,4,5,6,7] 和 k = 3
    输出: [5,6,7,1,2,3,4]
    解释:
        向右旋转 1 步: [7,1,2,3,4,5,6]
        向右旋转 2 步: [6,7,1,2,3,4,5]
        向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:
    输入: [-1,-100,3,99] 和 k = 2
    输出: [3,99,-1,-100]
    解释:
        向右旋转 1 步: [99,-1,-100,3]
        向右旋转 2 步: [3,99,-1,-100]

说明:
    尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    要求使用空间复杂度为 O(1) 的 原地 算法。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    #
    def rotate_1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_size = len(nums)
        cnt = 0
        for idx in range(0, k):
            tmp = nums[idx]
            jdx, jdx_new = idx, (idx-k) % nums_size
            while jdx_new != idx:
                nums[jdx] = nums[jdx_new]
                jdx, jdx_new = jdx_new, (jdx_new - k) % nums_size
                cnt += 1
            nums[jdx] = tmp
            cnt += 1
            if cnt == nums_size:
                break

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_size = len(nums)
        k = k % nums_size

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 将整个序列倒序
        reverse(0, nums_size-1)
        # 将 nums[:k] 倒序 & 将 nums[k:] 倒序
        reverse(0, k-1)
        reverse(k, nums_size-1)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
nums = [-1]
k = 2
Solution().rotate(nums, k)
print(nums)
