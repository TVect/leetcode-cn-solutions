"""
给你一个数组 nums ，请你完成两类查询，其中一类查询要求更新数组下标对应的值，另一类查询要求返回数组中某个范围内元素的总和。

实现 NumArray 类：
NumArray(int[] nums) 用整数数组 nums 初始化对象
void update(int index, int val) 将 nums[index] 的值更新为 val
int sumRange(int left, int right) 返回子数组 nums[left, right] 的总和（即，nums[left] + nums[left + 1], ..., nums[right]）
 

示例：
    输入：
        ["NumArray", "sumRange", "update", "sumRange"]
        [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    输出：
        [null, 9, null, 8]
    解释：
        NumArray numArray = new NumArray([1, 3, 5]);
        numArray.sumRange(0, 2); // 返回 9 ，sum([1,3,5]) = 9
        numArray.update(1, 2);   // nums = [1,2,5]
        numArray.sumRange(0, 2); // 返回 8 ，sum([1,2,5]) = 8

提示：
    1 <= nums.length <= 3 * 10^4
    -100 <= nums[i] <= 100
    0 <= index < nums.length
    -100 <= val <= 100
    0 <= left <= right < nums.length
    最多调用 3 * 10^4 次 update 和 sumRange 方法

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-mutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_size = len(nums)
        self.segment_tree = [-1] * (self.nums_size * 2)
        # initialize segment tree
        # self.segment_tree[nums_size, nums_size + 1, ..., 2 * nums_size - 1] = nums
        for idx in range(2*self.nums_size-1, self.nums_size-1, -1):
            self.segment_tree[idx] = nums[idx-self.nums_size]
        # 每个节点 idx 的左子节点为 idx * 2, 右子节点为 idx * 2 + 1
        for idx in range(self.nums_size-1, -1, -1):
            self.segment_tree[idx] = self.segment_tree[idx * 2] + self.segment_tree[idx * 2 + 1]
        print(self.segment_tree)

    def update(self, index: int, val: int) -> None:
        node_idx = self.nums_size + index
        diff = val - self.segment_tree[node_idx]
        while node_idx:
            self.segment_tree[node_idx] += diff
            node_idx //= 2

    def sumRange(self, left: int, right: int) -> int:
        left = left + self.nums_size
        right = right + self.nums_size
        summation = 0
        while left <= right:
            if left % 2 == 1:
                # left 位于右子树上
                summation += self.segment_tree[left]
                left += 1
            if right % 2 == 0:
                # right 位于左子树上
                summation += self.segment_tree[right]
                right -= 1
            left //= 2
            right //= 2
        return summation


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
