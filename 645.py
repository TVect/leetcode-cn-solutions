"""
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，
导致集合 丢失了一个数字 并且 有一个数字重复 。
给定一个数组 nums 代表了集合 S 发生错误后的结果。
请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1：
    输入：nums = [1,2,2,4]
    输出：[2,3]

示例 2：
    输入：nums = [1,1]
    输出：[1,2]
 

提示：
    2 <= nums.length <= 104
    1 <= nums[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-mismatch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import collections


class Solution:

    # 使用 hashset
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        n = len(nums)
        dup, miss = -1, -1
        for i in range(n + 1):
            if cnt[i] == 2:
                dup = i
            if cnt.get(i, 0) == 0:
                miss = i
        return [dup, miss]

    # 使用索引对应
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, miss = -1, -1
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                dup = abs(num)
            nums[idx] = -abs(nums[idx])
        for idx, num in enumerate(nums):
            if num > 0:
                miss = idx + 1
        return [dup, miss]


nums = [1, 2, 2, 4]
print(Solution().findErrorNums(nums))